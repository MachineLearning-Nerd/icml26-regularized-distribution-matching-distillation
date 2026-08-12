# Claim 4 toy output

This directory stores the output of `src/claim4_rdmd_2d_toy.py`.

The program is a disclosed deterministic assignment surrogate for the paper's 2-D Gaussian-to-8-Gaussian experiment. It is not a trained RDMD model, does not run diffusion score matching, and does not reproduce the paper's 5,000-sample/MLP/100k-iteration protocol.

The checked-in `results.csv` contains three seeds at each of `lambda=0`, `0.2`, and `1.0`. The rows are identical across lambda values, so this run observed no regularization effect. The output must not be used as evidence that RDMD exhibits the paper's reported quality/faithfulness trade-off.

The files are covered by `SHA256SUMS`. Verify them from this directory:

```bash
sha256sum -c SHA256SUMS
```
