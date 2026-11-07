# P2 LaTeX and arXiv build

## Dependencies

- Pandoc;
- TeX Live with `latexmk`, `natbib`, `microtype`, `booktabs` and `hyperref`;
- Inkscape for deterministic SVG-to-PDF conversion.

## Build

```bash
chmod +x build.sh arxiv_pack.sh
./build.sh
```

Outputs:

- `body.tex` generated from the canonical Markdown manuscript;
- vector figures converted to PDF;
- `main.pdf`;
- `BUILD_RECEIPT.txt` and SHA-256 manifest.

## arXiv package

```bash
./arxiv_pack.sh
```

The script recompiles from an isolated `arxiv-src` directory and creates:

- `P2_ARXIV_SOURCE.tar.gz`;
- isolated compiled PDF;
- package receipt and SHA-256 manifest.

No generated PDF or tarball is canonical until its receipt has been committed or archived in the versioned release.
