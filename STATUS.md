# Status

- Repository: https://github.com/MachineLearning-Nerd/icml26-regularized-distribution-matching-distillation
- Former name: icml26-repro-KpaQc72q7m-one-step-optimal-transport-rdmd
- Paper: Regularized Distribution Matching Distillation for One-step Unpaired Image-to-Image Translation
- Authors: Denis Rakitin, Ivan Shchekotov, and Dmitry Vetrov
- Venue: Structured Probabilistic Inference & Generative Modeling workshop of ICML 2024; the icml26 prefix is the collection prefix.
- OpenReview: KpaQc72q7m
- arXiv: 2406.14762v1
- Branches: main only; canonical/default branch
- Commit identity: MachineLearning-Nerd
- Compute: local CPU/local GTX 1050 only; no remote/HF/paid compute.

| Claim | Local status |
| --- | --- |
| C1 — theoretical optimum converges to the quadratic-cost Monge map | INCONCLUSIVE_SOURCE_CPU_AUDIT |
| C2 — RDMD objective and coordinate-descent production path | SOURCE_AUDITED_UNVERIFIED |
| C3 — AFHQv2 Cat-to-Wild quality/faithfulness result | PAPER_REPORTED_UNVERIFIED |
| C4 — 2-D Gaussian-to-8-Gaussian lambda trade-off | NON_REPRODUCING_TOY |
| C5 — Appendix A soft-to-hard convergence proof | SOURCE_AUDITED_UNVERIFIED |

Overall verdict: **INCONCLUSIVE_SCOPED_TO_SOURCE_AND_BOUNDED_TOY**. The pinned paper source and existing audit artifacts are preserved, but no full RDMD implementation, checkpoint, dataset, training log, theorem-prover artifact, or benchmark result is independently reproduced. Publication of full-paper results is not allowed.

Evidence: CLAIM_EVIDENCE.md, SOURCE_AUDIT.md, EVIDENCE_MANIFEST.json, evidence/claim1_attempt1/, evidence/source/, outputs/claim4_rdmd_2d_toy/, and contract/live_claims.json.
