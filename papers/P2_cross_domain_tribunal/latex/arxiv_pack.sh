#!/usr/bin/env bash
set -euo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
cd "$HERE"
./build.sh

rm -rf arxiv-src
mkdir -p arxiv-src/figures
cp main.tex body.tex figures_appendix.tex tables_appendix.tex references.bib arxiv-src/
cp figures/*.pdf arxiv-src/figures/ 2>/dev/null || true
cp ../CLAIM_LEDGER.csv ../CASE_MATRIX.csv ../CITATION_CLAIM_MAP.csv arxiv-src/

(cd arxiv-src && latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex)
rm -f arxiv-src/*.aux arxiv-src/*.bbl arxiv-src/*.blg arxiv-src/*.fdb_latexmk arxiv-src/*.fls arxiv-src/*.log arxiv-src/*.out

tar -czf P2_ARXIV_SOURCE.tar.gz -C arxiv-src .
sha256sum P2_ARXIV_SOURCE.tar.gz arxiv-src/main.pdf > ARXIV_PACKAGE_SHA256SUMS.txt
printf 'PASS_P2_ARXIV_PACKAGE\n' > ARXIV_PACKAGE_RECEIPT.txt
cat ARXIV_PACKAGE_SHA256SUMS.txt >> ARXIV_PACKAGE_RECEIPT.txt
