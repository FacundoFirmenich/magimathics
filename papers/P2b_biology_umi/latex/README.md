# P2b LaTeX and bioRxiv build

## Dependencies

- Pandoc;
- TeX Live with `latexmk`, `natbib`, `microtype`, `booktabs` and `hyperref`;
- Inkscape for deterministic SVG-to-PDF conversion.

## Build

```bash
chmod +x build.sh biorxiv_pack.sh
./build.sh
```

Outputs:

- `body.tex` generated from the canonical Markdown manuscript;
- vector figures converted to PDF;
- `main.pdf`;
- `BUILD_RECEIPT.txt` and SHA-256 manifest.

## bioRxiv package

```bash
./biorxiv_pack.sh
```

The script recompiles from an isolated `biorxiv-src` directory and creates:

- `P2B_BIORXIV_SOURCE.tar.gz`;
- isolated compiled PDF;
- package receipt and SHA-256 manifest.

The final source archive is not canonical until the compiled receipt, citation-key audit and evidence ledger have all passed.
