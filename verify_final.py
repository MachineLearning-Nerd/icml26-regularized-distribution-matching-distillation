import csv
import hashlib
import json
import pathlib
import subprocess
import tarfile


ROOT = pathlib.Path(__file__).resolve().parent
REPOSITORY = "https://github.com/MachineLearning-Nerd/icml26-regularized-distribution-matching-distillation"
FORMER_REPOSITORY = "https://github.com/MachineLearning-Nerd/icml26-repro-KpaQc72q7m-one-step-optimal-transport-rdmd"
IDENTITY = "MachineLearning-Nerd"
EMAIL = "37579156+MachineLearning-Nerd@users.noreply.github.com"
OVERALL = "INCONCLUSIVE_SCOPED_TO_SOURCE_AND_BOUNDED_TOY"
EXPECTED_STATUSES = {
    "C1": "INCONCLUSIVE_SOURCE_CPU_AUDIT",
    "C2": "SOURCE_AUDITED_UNVERIFIED",
    "C3": "PAPER_REPORTED_UNVERIFIED",
    "C4": "NON_REPRODUCING_TOY",
    "C5": "SOURCE_AUDITED_UNVERIFIED",
}


def run(*args):
    result = subprocess.run(args, cwd=ROOT, check=True, capture_output=True, text=True)
    return result.stdout


def fail(message):
    print("FINAL_AUDIT=FAILED " + message)
    raise SystemExit(1)


def load(relative):
    try:
        return json.loads((ROOT / relative).read_text())
    except Exception as exc:
        fail("invalid_json=" + relative + ":" + str(exc))


def require_files():
    required = [
        ".gitignore",
        "README.md",
        "STATUS.md",
        "AUTONOMOUS_STATE.json",
        "CLAIM_EVIDENCE.md",
        "SOURCE_AUDIT.md",
        "ENVIRONMENT.md",
        "REPORT.md",
        "AUTHOR_THANK_YOU.md",
        "CITATION.cff",
        "BRANCH_AUDIT.md",
        "branch-audit.md",
        "claims.json",
        "contract/live_claims.json",
        ".trackio/logbook/pages/claim-1-theorem-ot-limit/page.md",
        ".trackio/logbook/pages/claim-4-rdmd-toy/page.md",
        "evidence/claim1_attempt1/SOURCE_AUDIT.md",
        "evidence/claim1_attempt1/source_excerpt.tex",
        "evidence/source/SHA256SUMS",
        "evidence/source/arxiv-2406.14762.pdf",
        "evidence/source/arxiv-2406.14762-source.tar.gz",
        "outputs/claim1_attempt1/SHA256SUMS",
        "outputs/claim4_rdmd_2d_toy/README.md",
        "outputs/claim4_rdmd_2d_toy/SHA256SUMS",
        "outputs/claim4_rdmd_2d_toy/config.json",
        "outputs/claim4_rdmd_2d_toy/raw.json",
        "outputs/claim4_rdmd_2d_toy/results.csv",
        "outputs/claim4_rdmd_2d_toy/summary.json",
        "src/claim1_source_audit.py",
        "src/claim4_rdmd_2d_toy.py",
        "tests/test_claim1_source_audit.py",
        "tests/test_claim4.py",
        "EVIDENCE_MANIFEST.json",
        "verify_final.py",
    ]
    missing = [path for path in required if not (ROOT / path).is_file()]
    if missing:
        fail("missing=" + ",".join(missing))


def check_git():
    if run("git", "branch", "--show-current").strip() != "main":
        fail("branch_is_not_main")
    remote = run("git", "remote", "get-url", "origin").strip().removesuffix(".git")
    if remote != REPOSITORY:
        fail("remote=" + remote)
    branches = run("git", "for-each-ref", "refs/heads", "--format=%(refname:short)").splitlines()
    if branches != ["main"]:
        fail("local_branches=" + ",".join(branches))
    if run("git", "for-each-ref", "refs/original", "--format=%(refname)").strip():
        fail("original_refs_present")
    if int(run("git", "rev-list", "--count", "main").strip()) < 6:
        fail("canonical_history_too_short")
    for line in run("git", "log", "main", "--format=%H%x00%an%x00%ae%x00%cn%x00%ce%x00%s").splitlines():
        parts = line.split("\x00", 5)
        if len(parts) != 6 or parts[1] != IDENTITY or parts[2] != EMAIL or parts[3] != IDENTITY or parts[4] != EMAIL:
            fail("noncanonical_commit_identity=" + line)
    if "Co-authored-by:" in run("git", "log", "main", "--format=%B"):
        fail("coauthor_trailer_present")


def check_json_contract():
    state = load("AUTONOMOUS_STATE.json")
    if state["github_repository"] != REPOSITORY or state["former_github_repository"] != FORMER_REPOSITORY:
        fail("state_repository_mismatch")
    if state["phase"] != "published_and_verified" or state["branch_set"] != ["main"]:
        fail("state_phase_or_branches")
    if state["overall_verdict"] != OVERALL or state["publication_allowed"] is not False:
        fail("state_verdict")
    if state["claim_statuses"] != EXPECTED_STATUSES:
        fail("state_claim_statuses")
    claims = load("claims.json")
    if claims["repository"] != REPOSITORY or claims["former_repository"] != FORMER_REPOSITORY:
        fail("claims_repository_mismatch")
    if claims["overall_verdict"] != OVERALL or claims["publication_allowed"] is not False:
        fail("claims_verdict")
    if {item["id"]: item["status"] for item in claims["claims"]} != EXPECTED_STATUSES:
        fail("claims_statuses")
    contract = load("contract/live_claims.json")
    if contract["orid"] != "KpaQc72q7m" or contract["arxiv"] != "2406.14762" or len(contract["claims"]) != 5:
        fail("contract_identity_or_claim_count")


def check_checksum_file(relative):
    checksum_path = ROOT / relative
    for line in checksum_path.read_text().splitlines():
        if not line.strip():
            continue
        expected, name = line.split(maxsplit=1)
        name = name.lstrip("*")
        root_target = ROOT / name
        target = root_target if root_target.is_file() else checksum_path.parent / name
        if not target.is_file():
            fail("checksum_target_missing=" + name)
        if hashlib.sha256(target.read_bytes()).hexdigest() != expected:
            fail("checksum_mismatch=" + str(target.relative_to(ROOT)))


def check_source():
    check_checksum_file("evidence/source/SHA256SUMS")
    check_checksum_file("outputs/claim1_attempt1/SHA256SUMS")
    check_checksum_file("outputs/claim4_rdmd_2d_toy/SHA256SUMS")
    archive = ROOT / "evidence/source/arxiv-2406.14762-source.tar.gz"
    with tarfile.open(archive, "r:gz") as handle:
        members = handle.getmembers()
        if len(members) != 32 or sum(item.isfile() for item in members) != 26 or sum(item.isdir() for item in members) != 6:
            fail("source_archive_inventory")
        if any(item.issym() or (item.isfile() and item.mode & 0o111) for item in members):
            fail("source_archive_permissions")
        if "main.tex" not in {item.name for item in members}:
            fail("main_tex_missing")


def check_toy():
    config = load("outputs/claim4_rdmd_2d_toy/config.json")
    if config["n"] != 160 or config["seeds"] != [17, 23, 31] or config["lambdas"] != [0, 0.2, 1.0]:
        fail("toy_config")
    summary = load("outputs/claim4_rdmd_2d_toy/summary.json")
    if summary["verdict"] != "non_reproducing_toy" or summary["observed_lambda_effect"] is not False:
        fail("toy_verdict")
    if "not trained RDMD" not in summary["scope"]:
        fail("toy_scope")
    means = summary["means"]
    if set(means) != {"0.0", "0.2", "1.0"} or len({json.dumps(means[key], sort_keys=True) for key in means}) != 1:
        fail("toy_lambda_effect")
    with (ROOT / "outputs/claim4_rdmd_2d_toy/results.csv").open(newline="") as handle:
        rows = list(csv.DictReader(handle))
    if len(rows) != 9 or {row["lambda"] for row in rows} != {"0.0", "0.2", "1.0"}:
        fail("toy_csv_shape")


def check_manifest():
    manifest = load("EVIDENCE_MANIFEST.json")
    if manifest["schema_version"] != 1:
        fail("manifest_schema")
    tracked = [path for path in run("git", "ls-files", "-z").split("\x00") if path]
    expected = sorted(path for path in tracked if path not in {"AUTONOMOUS_STATE.json", "EVIDENCE_MANIFEST.json"})
    actual = sorted(item["path"] for item in manifest["files"])
    if actual != expected:
        fail("manifest_paths")
    for item in manifest["files"]:
        target = ROOT / item["path"]
        if hashlib.sha256(target.read_bytes()).hexdigest() != item["sha256"] or target.stat().st_size != item["bytes"]:
            fail("manifest_hash=" + item["path"])


def main():
    require_files()
    check_git()
    check_json_contract()
    check_source()
    check_toy()
    check_manifest()
    print("FINAL_AUDIT=VERIFIED branches=1 claims=C1:inconclusive_source_cpu_audit,C2:source_audited_unverified,C3:paper_reported_unverified,C4:non_reproducing_toy,C5:source_audited_unverified publication_allowed=false")


if __name__ == "__main__":
    main()
