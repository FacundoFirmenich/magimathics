#!/usr/bin/env python3
from pathlib import Path
import sympy as sp

root = Path(__file__).resolve().parents[1]

n = sp.symbols("n", integer=True, positive=True)
assert sp.limit(10**(n+1)*sp.sin(sp.pi*10**(-n)/180), n, sp.oo) == sp.pi/18

u = sp.pi/6
assert sp.simplify(6*u-sp.pi) == 0
assert sp.simplify(8*u-4*sp.pi/3) == 0
assert sp.simplify(12*u-2*sp.pi) == 0
assert sp.simplify(24*u-4*sp.pi) == 0

theta = sp.symbols("theta", positive=True)
res = sp.Rational(1,2)*(theta-sp.sin(theta)*sp.cos(theta))
assert sp.series(res,theta,0,7).removeO().coeff(theta,3) == sp.Rational(1,3)

alpha = sp.symbols("alpha", real=True)
assert sp.solve(sp.Eq(2**(alpha/2),2),alpha) == [sp.Integer(2)]

required = [
    "README.md",
    "docs/00_SUPERDOCUMENTO_MAGIMATICS.md",
    "docs/01_TABLA_ROSETTA.md",
    "docs/02_FORMULARIO_CANONICO.md",
    "docs/03_ESTADO_DEL_ARTE_Y_FRONTERA.md",
    "docs/04_HIPERCORPUS_CANONICO.md",
    "docs/05_GENEALOGIA_DE_CORRECCIONES.md",
    "docs/06_PROGRAMA_ESTRATEGICO.md",
    "docs/07_BIBLIOGRAFIA.md",
    "docs/08_PROCEDENCIA_Y_LIMITES.md",
    "docs/09_HERENCIA_MAGIMATICS_PREVIA.md",
    "data/master_claim_ledger.csv",
]
for rel in required:
    p = root/rel
    assert p.exists() and p.stat().st_size > 0, rel

print("PASS_MAGIMATICS_CORPUS")
print("q_obs = pi/18")
print("UMI ladder = 6, 8, 12, 24")
print("epistemic residual leading term = theta^3/3")
print("quadratic selector alpha = 2")
