#!/usr/bin/env python3
from fractions import Fraction
import csv
from pathlib import Path

R=Path(__file__).resolve().parent
mu=Fraction(31,100)
P=lambda nu:(Fraction(577)+48*nu)/Fraction(772)
q=Fraction(24,169)
sf=Fraction(193,208)
assert q*sf==Fraction(579,4394)
assert P(mu)>Fraction(3,4)
assert P(mu**3)<Fraction(3,4)
assert mu**2 < Fraction(1)/(24*mu)
rows=list(csv.DictReader((R/'QBRAID_SIM_RECEIPT.csv').open()))
assert len(rows)==8
for row in rows:
    assert abs(float(row['program_accept'])-float(q))<2e-15
    assert abs(float(row['filter_accept'])-float(sf))<3e-15
    assert abs(float(row['combined_accept'])-float(q*sf))<3e-15
    assert abs(float(row['sign_mean'])-float(mu**2))<4e-15
    target=P(mu) if row['arm']=='enriched' else P(mu**3)
    assert abs(float(row['phase_correct_conditional'])-float(target))<3e-15
print('PASS_SC43M_FREEZE')
print('mu = 31/100')
print('pair program acceptance = 24/169')
print('filter acceptance = 193/208')
print('combined acceptance = 579/4394')
print('marginal phase success =',P(mu**3))
print('enriched phase success =',P(mu))
print('qBraid statevector replay = 8/8 exact within numerical tolerance')
print('QPU execution = PENDING EXPLICIT CONFIRMATION')
