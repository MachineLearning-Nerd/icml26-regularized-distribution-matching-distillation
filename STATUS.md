# Status

- Classification: paper-associated, source-pinned local reproduction audit.
- Paper: `Regularized Distribution Matching Distillation for One-step Unpaired Image-to-Image Translation`.
- Authors: Denis Rakitin, Ivan Shchekotov, and Dmitry Vetrov.
- Venue note: the pinned paper is an ICML 2024 workshop paper; `icml26` is the collection prefix, not the paper venue.
- OpenReview ID: `KpaQc72q7m`.
- Source pinned: arXiv `2406.14762v1` PDF/source archive; checksums are in `evidence/source/SHA256SUMS`.
- Compute: local CPU/local GTX 1050 only; no remote, paid, Hugging Face, or other external compute.
- Claim 1: **inconclusive** after a source/CPU feasibility audit; finite optimization cannot verify or falsify the theoretical-optimum theorem.
- Claim 4: **non-reproducing toy**; the reduced assignment surrogate produces identical metrics at `lambda=0`, `0.2`, and `1.0` and therefore does not show the paper's reported trade-off.
- Claims 2, 3, and 5: source-audited or paper-reported, but not independently reproduced here.
- Publication allowed: `false`.
- Next: independent review of the Claim 1 audit; a faithful reproduction would require implementing the paper's diffusion models and obtaining the required data/checkpoints/compute.
