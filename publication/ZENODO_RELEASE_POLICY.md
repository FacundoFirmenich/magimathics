# Zenodo release policy

## Canonical chain

1. Develop on GitHub with `main` as the canonical branch.
2. Freeze the manuscript claims and proof objects.
3. Run independent verification from a clean checkout.
4. Create a semantic-version release.
5. Archive the exact release in Zenodo.
6. Record the version DOI and concept DOI in README/CITATION metadata.
7. Cross-link arXiv/EarthArXiv/bioRxiv and the eventual journal DOI.

## Large artifacts

Large datasets, checkpoints, PDFs, ZIP bundles and generated figures must not be committed as ordinary Git blobs. Store them in the GitHub Release and/or Zenodo deposit, accompanied by SHA-256 manifests.

## DOI semantics

- The Zenodo concept DOI identifies the evolving repository lineage.
- Each tagged release receives a version DOI.
- The manuscript/preprint and journal article have their own bibliographic identifiers.
- Related identifiers must state whether a record `isSupplementTo`, `isVersionOf`, `isDocumentedBy`, or `isSourceOf` another object.
