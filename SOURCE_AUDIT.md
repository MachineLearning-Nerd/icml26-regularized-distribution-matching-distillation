# Source audit

## Pinned paper artifacts

| Artifact | Path | SHA-256 |
| --- | --- | --- |
| arXiv PDF, version 1 | evidence/source/arxiv-2406.14762.pdf | a986167d9f354b86aea38a1073bb888da97fd39a2ce40afd3f19ef5a7e86bb24 |
| arXiv source archive, version 1 | evidence/source/arxiv-2406.14762-source.tar.gz | b94ec5ee2e7a223237e597569fc86149ee9483300bceecba074bf6d209d139ac |

The checksum file at evidence/source/SHA256SUMS is checked by verify_final.py. The source archive contains 32 members: 26 regular files and 6 directories, with no symlinks and no executable regular files. The archive includes the paper manuscript, figures, bibliography, styles, and texput.log; it contains no runnable RDMD implementation or trained weights.

## Archive member inventory

The following hashes are computed over the uncompressed contents of each regular archive member.

~~~text
+48d18794a5d97c0479a588cc2eac0917992feb9da83acc4631b8f55757d80f9b  algorithmic.sty
93fd0eb31c112eb405833db8f1d7f5d238c7e691b1c05680d7276e68f36d564a  algorithm.sty
6453c789c2e7aab59dda039275e9aeca3d6cbff9c1ed13f8ab62b13528e7ef52  appendix/B_sigma_ablation.tex
1d0ae5d831327058792bbcd483473abf5143c2b8376b6bf1026299d1941c0635  appendix/A_proofs.tex
0710b4a03bd3b1d26f8520983c0ce918cad5bd6a4fd27bc9d9a6e2e50d252248  appendix/C_details.tex
b56ec4434b9f4607529a4b23dc68ad8d4b94f1f631c8cddaf7da78140d53a5ea  fancyhdr.sty
3a69e73c9c8968bd555204d84e59616f3c4fd23c5fd6994502167860bd8a2849  icml2024.bst
dcc3e9490d935516b4561b2cd84c64ffb87f17bb9ba4be0c7401763b01017598  icml2024.sty
6821b259f63c572b4cb5a838980ee23fc29dcff11f8acb868c7a2d85b741b60d  images/mnist/mnist_init_visual.png
d9d2bec840c64420da1d8c51b0be1265a866ecec56a62fa37ecbc4a5435b6b5c  images/surface.png
cbe52826edaf2f3ccda9544fb9b06e4d2f4e5a43ad6db69193c93b7e18f2e4d7  images/c2w/title_pic.png
e66a4bdcdeae8e8e6b2465fc83ce593253a00f14d849beec4600f0c3b26acdb9  images/c2w/c2w_compare_new.png
77e754bf3addd1efd5a478753de0806a1b0be31e24274664a36be351283e7446  images/c2w/metrics_icml.png
31c13246f0913bb971ca8c3db0cd2022170ca072ced50d83613bcf98c6d651f4  images/toy_exps/toy.png
580f4ec42f861cd9fdc049a89d7ca344560108152e33b3121b4a8cd5639e9809  main.bbl
17b4b7e07225500de237fcf7c4488d37209b163e612f6903f5f49212d80356b7  main.tex
16a1cfd1c2810d29558a694b2e73c4dfeb57016f9659126d18bdcd57751a33f3  notation.tex
520cd3ca82cfc190897ed3ba54db6e97d17a0d536a16d30d4c0db8e067edbb58  references.bib
96bf97da5e69b8b2e9547897f5d20193207c5769fc5bd62a5ec91992da24cbc1  sections/4_related.tex
3be88d113359b8b6ead6f376ec37b225af64782db3cc76604b9c4dabeac47591  sections/5_experiments.tex
66821ecf778ec1d6c02a9c70e472475eb89078c3f33cd60e71e1da6267eb2043  sections/1_intro.tex
cea44080822d3399863e9b7b90fc2c46273f1029a435c96245709909fa3ebd99  sections/7_acknowledgements.tex
0c472569852d927874707fe3459d98fcb4e31ddf0cffa672b798b2ad27e91bc2  sections/2_background.tex
130a4e07ee4b345b2ef2a9c9c85d8c001a42e7ec48562da0931e8253ed6268ca  sections/3_method.tex
70090581194ff939079d396dc7fb5302506ababf2bc9ba549eff1a94e2eab1a7  sections/6_discussion.tex
dae764f719a9b25bb849025b660450accddd6309b00b309ea452b89cb5226aab  texput.log
~~~

## Existing Claim 1 and Claim 4 evidence

- evidence/claim1_attempt1/SOURCE_AUDIT.md and source_excerpt.tex are checksum-pinned by outputs/claim1_attempt1/SHA256SUMS.
- outputs/claim4_rdmd_2d_toy/ is checksum-pinned and records the exact configuration, raw rows, CSV, summary, and non-reproducing lambda result.

The archive and these derived artifacts establish traceability and a bounded audit scope. They do not independently establish the paper’s theorem, proof, training, or benchmark claims.
