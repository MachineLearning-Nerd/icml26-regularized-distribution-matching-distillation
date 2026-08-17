# Claim-to-evidence audit

This dossier separates the paper’s claims, how each claim is produced, and what this repository actually verifies. The pinned source is the primary reference for paper production paths; paper-reported numbers are not independent reproduction evidence.

## Paper identity

- Title: Regularized Distribution Matching Distillation for One-step Unpaired Image-to-Image Translation
- Authors: Denis Rakitin, Ivan Shchekotov, and Dmitry Vetrov
- arXiv: 2406.14762v1
- OpenReview: KpaQc72q7m
- Repository: https://github.com/MachineLearning-Nerd/icml26-regularized-distribution-matching-distillation

## Claim ledger

### C1 — theoretical optimal-transport limit

Paper claim: Under quadratic transport cost and mild regularity conditions, the theoretical RDMD optimum converges in probability to the Monge optimal-transport map as lambda approaches zero.

Paper production path: Section 3.2 defines the soft RDMD objective, states the theoretical optimum G^lambda, and gives the convergence claim. Appendix A states assumptions about bounded supports/densities, quadratic cost, positive bounded KL weighting, and continuous noise scale, then argues existence, weak compactness, lower semicontinuity, and convergence. Source anchors: sections/3_method.tex lines 42–50 and appendix/A_proofs.tex lines 63–97.

Local evidence: evidence/claim1_attempt1/SOURCE_AUDIT.md and source_excerpt.tex pin the theorem wording and its capacity/optimizer qualifications. A finite CPU optimizer cannot establish or falsify this universal theoretical statement.

Status: INCONCLUSIVE_SOURCE_CPU_AUDIT.

### C2 — RDMD objective and training procedure

Paper claim: RDMD combines a diffusion-distribution matching KL term with lambda times expected transport cost and optimizes the generator/fake diffusion model by coordinate descent.

Paper production path: Section 3.1 replaces the Gaussian input with source samples, adds the transport penalty, uses a pretrained target score and fake diffusion model, and alternates generator and fake-model objectives. Source anchor: sections/3_method.tex lines 3–30.

Local evidence: The pinned source preserves the objective and equations. No runnable generator, target/fake score models, coordinate-descent implementation, checkpoint, or training log is present.

Status: SOURCE_AUDITED_UNVERIFIED.

### C3 — AFHQv2 Cat-to-Wild benchmark

Paper claim: On 64x64 AFHQv2 Cat-to-Wild translation, RDMD reports a quality/faithfulness trade-off, including FID 6.93 at lambda=0.05 and stronger SSIM/near-stronger PSNR in the reported transport-cost range.

Paper production path: Pretrain the EDM target model on AFHQv2, train five RDMD generators for the stated lambda grid, run ILVR/SDEdit/EGSDE baselines, and recompute FID, L2, PSNR, and SSIM on the same test data. Source anchor: sections/5_experiments.tex lines 33–49.

Local evidence: The paper source and figures are pinned. No AFHQv2 data, model weights, training code, baseline implementation, evaluator, predictions, or metric table is present.

Status: PAPER_REPORTED_UNVERIFIED.

### C4 — 2-D Gaussian-to-8-Gaussian trade-off

Paper claim: The toy experiment shows that lambda=0.2 balances target-distribution fidelity and input-output correspondence by reducing trajectory intersections relative to unregularized distillation.

Paper production path: Train the paper’s MLP target/fake diffusion/generator system on 5,000 source and target samples, sweep lambda, and measure transport cost, target-distribution fidelity, and line-segment intersections. Source anchor: sections/5_experiments.tex lines 8–14.

Local evidence: outputs/claim4_rdmd_2d_toy/ contains a deterministic assignment surrogate with 160 samples, three seeds, and lambda values 0, 0.2, and 1.0. All lambda rows are identical and observed_lambda_effect is false. The artifact is a negative diagnostic, not a neural RDMD reproduction.

Status: NON_REPRODUCING_TOY.

### C5 — Appendix A convergence proof

Paper claim: Appendix A gives the formal soft-to-hard convergence argument supporting asymptotic optimality.

Paper production path: Independently audit the assumptions, existence of minima, tightness/weak convergence, lower semicontinuity of the objective, uniqueness of the quadratic Monge map, and the limiting chain of inequalities. Source anchor: appendix/A_proofs.tex lines 1–97 and lines 227 onward.

Local evidence: Appendix A is preserved inside the source archive and the source excerpt records the proof setup. No independent formal proof audit, theorem-prover artifact, or author-controlled proof certificate is present.

Status: SOURCE_AUDITED_UNVERIFIED.

## Overall boundary

The local result is INCONCLUSIVE_SCOPED_TO_SOURCE_AND_BOUNDED_TOY. The repository supports source traceability, a finite non-reproducing toy, and an honest CPU feasibility boundary. It does not reproduce the RDMD theorem, proof, neural training, AFHQv2 benchmark, or reported metrics.
