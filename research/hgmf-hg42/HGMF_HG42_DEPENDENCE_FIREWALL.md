# HGMF‑HG42 — Dependence firewall

## Authorized rules

### Weighted mean

For fixed nonnegative weights summing to one,

E = sum_k w_k E_k

is an e-value under arbitrary dependence.

### Intersection minimum

E_all = min_k E_k

is an e-value and requires every cell to exceed the final evidence threshold if E_all is to exceed it.

### Sequential conditional product

E_t = product_{k<=t} e_k

is authorized only if

E[e_k | F_{k-1}] <= 1

under every null law and the filtration is frozen before holdout.

## Forbidden default

The product of marginally valid e-values is not authorized merely because each factor has expectation at most one.

A concrete counterexample has two identical factors:

E1=E2=2 with probability 1/2 and zero otherwise.

Each expectation equals one, while the product expectation equals two.

## Carrier implications

- pressure nodes cannot be multiplied as independent;
- interpolation nodes cannot be multiplied as independent;
- loop summaries cannot be multiplied if they share calibration error;
- repeated curves cannot be multiplied if training or covariance estimates leak across evaluation blocks;
- carrier e-values may be averaged with frozen weights under arbitrary dependence;
- a product across carriers requires conditional or independence authority, not intuition.
