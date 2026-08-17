# Environment and reproduction boundary

- Compute policy: local CPU/local GTX 1050 only.
- Remote, paid, upgraded-cloud, Hugging Face Jobs, and external GPU execution are out of scope.
- Existing local artifacts are dependency-light Python diagnostics and source audits.
- No RDMD training implementation, diffusion checkpoint, AFHQv2 dataset, baseline evaluator, or theorem-prover artifact is included.
- The pinned arXiv PDF/source archive is checked before interpreting paper claims.
- Generated Python bytecode, macOS metadata, and pytest cache are ignored.
- The lightweight final verifier uses Python 3, Git, JSON, tarfile, CSV, and SHA-256.

The environment is sufficient for source checks and the disclosed deterministic assignment toy. It is not evidence for the paper’s full training or benchmark claims.
