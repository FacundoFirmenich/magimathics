#!/usr/bin/env bash
set -euo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
cd "$HERE"
./build.sh

rm -rf biorxiv-src
mkdir -p biorxiv-src/figures
cp main.tex body.tex references.bib biorxiv-src/
cp figures/*.pdf biorxiv-src/figures/ 2>/dev/null || true
cp ../CLAIM_LEDGER.csv ../BIOLOGICAL_EVIDENCE_MATRIX.csv ../PRIMARY_EVIDENCE_LEDGER.csv ../CITATION_CLAIM_MAP.csv biorxiv-src/

(cd biorxiv-src && latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex)
rm -f biorxiv-src/*.aux biorxiv-src/*.bbl biorxiv-src/*.blg biorxiv-src/*.fdb_latexmk biorxiv-src/*.fls biorxiv-src/*.log biorxiv-src/*.out

tar -czf P2B_BIORXIV_SOURCE.tar.gz -C biorxiv-src .
sha256sum P2B_BIORXIV_SOURCE.tar.gz biorxiv-src/main.pdf > BIORXIV_PACKAGE_SHA256SUMS.txt
printf 'PASS_P2B_BIORXIV_PACKAGE\n' > BIORXIV_PACKAGE_RECEIPT.txt
cat BIORXIV_PACKAGE_SHA256SUMS.txt >> BIORXIV_PACKAGE_RECEIPT.txt
