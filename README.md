# RDMD: Source-Pinned Reproduction Audit

This repository contains an evidence-first audit of **Regularized Distribution Matching Distillation for One-step Unpaired Image-to-Image Translation**. It is a local reproduction workspace, not the authors' official implementation. The repository does not currently contain a full RDMD training pipeline, pretrained checkpoints, or a completed reproduction of the paper's benchmark results.

| Resource | Link |
| --- | --- |
| Repository | [MachineLearning-Nerd/icml26-regularized-distribution-matching-distillation](https://github.com/MachineLearning-Nerd/icml26-regularized-distribution-matching-distillation) |
| Paper | [arXiv:2406.14762](https://arxiv.org/abs/2406.14762) |
| OpenReview submission | [KpaQc72q7m](https://openreview.net/forum?id=KpaQc72q7m) |
| Pinned source version | [arXiv:2406.14762v1](https://arxiv.org/abs/2406.14762v1) |

## Classification and paper association

- **Collection classification:** paper-associated, source-pinned local reproduction audit.
- **Paper match:** direct. The pinned PDF and source archive contain the exact title and the authors Denis Rakitin, Ivan Shchekotov, and Dmitry Vetrov; the arXiv record independently confirms the same metadata.
- **Paper version:** arXiv v1, submitted 20 June 2024.
- **Venue note:** the pinned PDF says the work was accepted to the Structured Probabilistic Inference & Generative Modeling workshop of ICML 2024. The `icml26` prefix identifies this repository collection; it does not claim that this paper is an ICML 2026 paper.
- **OpenReview note:** the repository preserves the OpenReview identifier supplied by the collection. OpenReview may present a browser verification page, so the pinned arXiv PDF/source archive are the primary evidence used here.
- **Former repository name:** `icml26-repro-KpaQc72q7m-one-step-optimal-transport-rdmd`.

## Current status

**Overall result: incomplete and evidence-first.** The source artifacts are verified, Claim 1 has an inconclusive source/CPU feasibility audit, and Claim 4 has a reduced local toy. Neither result establishes the paper's theorem or benchmark numbers.

The local policy for this audit is CPU and the local GTX 1050 only. No remote, paid, Hugging Face, or other external compute was used. The machine-readable state records `publication_allowed: false`.

The Claim 4 artifact is especially important to interpret carefully: the checked-in deterministic assignment surrogate produces identical aggregate values for `lambda=0`, `0.2`, and `1.0`. It therefore does **not** reproduce the paper's reported regularization trade-off. This is recorded as a non-reproducing toy diagnostic, not as evidence for RDMD.

## What the paper does

RDMD modifies Distribution Matching Distillation for unpaired image-to-image translation. Instead of feeding the generator Gaussian noise, it feeds source-domain samples `x ~ p_source` and maps them to the target domain. The method combines:

1. a diffusion-distribution matching term between the generated and target distributions; and
2. a transport-cost penalty between each source input and its generated output.

The paper's conceptual objective is:

```text
L(theta) = integral omega_t KL(p_t^theta || p_t^target) dt
L^lambda(theta) = L(theta) + lambda E[c(x, G_theta(x))]
```

The practical procedure uses coordinate descent over a generator and a fake diffusion/denoising model, while a pretrained target diffusion model supplies the target score. The intended effect of `lambda` is a quality/faithfulness trade-off: low regularization favors target-distribution matching, while transport regularization encourages source-output correspondence.

The paper studies a 2-D Gaussian-to-8-Gaussian toy and unpaired AFHQv2 Cat-to-Wild translation. It reports one-step inference, rather than running the full multi-step diffusion sampler at inference time.

## What this repository contains

| Path | Purpose |
| --- | --- |
| `AUTONOMOUS_STATE.json` | Machine-readable phase, compute policy, next action, and claim outcomes |
| `STATUS.md` | Short human-readable audit status |
| `contract/live_claims.json` | Five paper claims tracked with explicit verification status |
| `evidence/source/arxiv-2406.14762.pdf` | Pinned paper PDF |
| `evidence/source/arxiv-2406.14762-source.tar.gz` | Pinned arXiv LaTeX source and figures |
| `evidence/source/SHA256SUMS` | Checksums for the pinned paper artifacts |
| `evidence/claim1_attempt1/SOURCE_AUDIT.md` | Claim 1 source and finite-CPU feasibility audit |
| `evidence/claim1_attempt1/source_excerpt.tex` | Pinned excerpt containing the theorem assumptions and proof setup |
| `outputs/claim1_attempt1/SHA256SUMS` | Checksum record for the Claim 1 audit artifacts |
| `outputs/claim4_rdmd_2d_toy/` | Generated output from the reduced Claim 4 diagnostic |
| `src/claim1_source_audit.py` | Explicit marker that Claim 1 is deferred to a proof-dependency audit |
| `src/claim4_rdmd_2d_toy.py` | Deterministic 2-D assignment surrogate; not neural RDMD training |
| `tests/test_claim1_source_audit.py` | Minimal source-audit consistency check |
| `tests/test_claim4.py` | Minimal output-generation check for the reduced toy |
| `.trackio/logbook/` | Short append-only audit notes for the Claim 1 and Claim 4 attempts |

The pinned source archive is a paper source snapshot. It contains LaTeX, bibliography, styles, and figures; it does not contain a runnable RDMD implementation or trained model weights.

## Branch inventory

The repository originally had two branches with different scopes:

| Branch | What it contained before cleanup | Final published state |
| --- | --- | --- |
| `main` | The authoritative audit: source pin, Claim 4 toy, and Claim 1 source/CPU audit | **Kept** as the only published branch |
| `master` | The initial source-pinning commit only; it did not contain the later audit artifacts | Default moved away, then stale remote branch removed |

The local `backup/pre-main-branch-cleanup` branch preserves the former `master` tip for rollback during this audit; it is not part of the published branch interface. The remote repository now exposes only `main`, which is also the default branch.

## Claim ledger: what each claim means and how it is produced

The claim IDs below correspond to `contract/live_claims.json`. They are claims made by the paper, not automatically validated facts. The “paper production path” describes what would have to be run or proved to support the claim; the “repository evidence” describes what this repository actually establishes.

| ID | Paper claim | Paper production path | Repository evidence | Status |
| --- | --- | --- | --- | --- |
| C1 | Under quadratic transport cost and mild regularity conditions, the theoretical optimum `G^lambda` converges in probability to the optimal transport map as `lambda -> 0` (Theorem 3.1 in the main text). | Define the soft RDMD objective, establish existence and convergence of its theoretical optima under the stated assumptions, and show convergence to the hard-constrained Monge optimum. This is a mathematical result, not a finite benchmark. | `evidence/claim1_attempt1/SOURCE_AUDIT.md` and the pinned theorem excerpt. The audit identifies the theorem's theoretical-optimum, capacity, and optimization qualifications. | **Inconclusive** |
| C2 | RDMD combines diffusion-distribution matching with an explicit transport-cost regularizer and trains the generator/fake diffusion model by coordinate descent. | Implement the target score, fake score, generator, noise schedule, KL surrogate, transport cost, and alternating optimization described in Section 3.1. | The source archive's `sections/3_method.tex` is pinned and inspected. No runnable implementation or training output is present in this repository. | **Source-audited; unverified here** |
| C3 | On AFHQv2 Cat-to-Wild at `64 x 64`, RDMD reports a quality/faithfulness trade-off, including FID `6.93` at `lambda=0.05`, compared with a pretrained diffusion FID of about `2.01`, and stronger SSIM/near-stronger PSNR in the reported transport-cost range. | Train the target diffusion model, train RDMD for the paper's regularization grid, run the ILVR/SDEdit/EGSDE baselines, and recompute FID, L2, PSNR, and SSIM on the same test data. | The values are present in the pinned paper source and figures only. The repository has no AFHQv2 data, checkpoints, benchmark script, or metric table. | **Paper-reported; unverified here** |
| C4 | In the 2-D Gaussian-to-8-Gaussian experiment, increasing `lambda` reduces trajectory intersections while changing target-distribution fidelity; `lambda=0.2` is reported as a useful trade-off. | Train the paper's MLP diffusion/fake-diffusion/generator system on 5,000 source and target samples for the stated schedule, then measure target-distribution distance, transport cost, and line-segment intersections across `lambda`. | `src/claim4_rdmd_2d_toy.py` runs a disclosed deterministic assignment surrogate and stores raw data, configuration, metrics, and hashes in `outputs/claim4_rdmd_2d_toy/`. Its three checked-in lambda rows are identical, so it does not reproduce the claimed trade-off. | **Non-reproducing toy** |
| C5 | The appendix supplies the formal proof supporting the soft-to-hard optimal-transport limit (the contract describes this as a gamma-convergence proof). | Independently check the appendix assumptions, existence argument, lower-semicontinuity steps, tightness argument, subsequence limit, uniqueness, and final convergence statement. | Appendix A is retained inside the pinned source archive and the source excerpt records its proof structure. No independent formal verification has been performed. The source presents a soft/hard objective and weak-convergence argument; this repository does not upgrade it to an independently verified gamma-convergence result. | **Source-audited; unverified here** |

### Claim 1 boundary

The local Claim 1 audit is deliberately narrow. The source states a theorem about a **theoretical optimum** and includes regularity assumptions plus the requirement that model capacity and optimization convergence be adequate. A finite CPU optimizer cannot establish or falsify that universal mathematical statement. No theorem prover artifact is present in the pinned source snapshot.

### Claim 4 boundary

The local toy preserves only a small set of concepts: 2-D Gaussian inputs, eight target centers, squared source-output cost, a radial target-fidelity proxy, and strict line-segment intersections. It does not implement:

- the paper's denoising networks;
- the diffusion objective or coordinate descent;
- the 5,000-sample training setup;
- the paper's Earth Mover's / discrete optimal-transport evaluation; or
- the AFHQv2 benchmark.

Because the generated `results.csv` has the same values for all three lambda settings, it is a useful negative diagnostic of the current surrogate, not a reproduction of Section 5.1.

## Reproduction boundary

This repository uses three separate labels:

1. **Paper-reported:** a number or conclusion printed in the pinned paper.
2. **Source-audited:** the paper source and its production path were pinned and inspected.
3. **Reproduced here:** an independent run produced stored, verifiable evidence for the relevant claim.

At the current audit point, C1 is inconclusive, C2 and C5 are source-audited but unverified, C3 is paper-reported but unverified, and C4 is a non-reproducing toy. No claim should be cited as independently reproduced from this repository.

## Verification commands

Run these commands from the repository root:

```bash
(cd evidence/source && sha256sum -c SHA256SUMS)
sha256sum -c outputs/claim1_attempt1/SHA256SUMS
(cd outputs/claim4_rdmd_2d_toy && sha256sum -c SHA256SUMS)
python3 -m pytest -q tests/test_claim1_source_audit.py tests/test_claim4.py
```

The test suite is intentionally small. Passing it verifies artifact shape and the reduced toy contract; it does not verify the paper's theorem or benchmark claims.

## Citation

If this audit or the paper is useful, please cite the paper:

```bibtex
@misc{rakitin2024rdmd,
  title={Regularized Distribution Matching Distillation for One-step Unpaired Image-to-Image Translation},
  author={Denis Rakitin and Ivan Shchekotov and Dmitry Vetrov},
  year={2024},
  eprint={2406.14762},
  archivePrefix={arXiv},
  primaryClass={cs.CV},
  note={Accepted to the Structured Probabilistic Inference and Generative Modeling workshop of ICML 2024},
  url={https://arxiv.org/abs/2406.14762}
}
```

## Thank you

Thank you to **Denis Rakitin, Ivan Shchekotov, and Dmitry Vetrov** for making the RDMD paper and its source materials available. Their work gives a clear setting for studying the tension between one-step diffusion distillation, unpaired image translation, and transport-based correspondence, and it makes the theoretical and experimental assumptions inspectable for reproduction work.
