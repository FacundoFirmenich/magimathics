# SC43-HXG — Hyperaccess Witness and Generative Discrimination

Primary jurisdiction: **HX-Q4-SIGN**.

## Exact result

For the principal Q4 envelope:

[
a=4/13,quad b=1/13,quad s_3=193/2197,quad a'=64/193,quad b'=1/193.
]

The optimal four-phase discrimination law is

[
P(
u)=rac{577+48
u}{772}.
]

The programmed instrument yields a branch sign (Cin{pm1}) with (mathbb E[C]=mu^2). Conditioned output coherence has magnitude (mu) and sign (C). Erasing the sign leaves coherence (mu^3).

Hence

[
P_{r_0}=P(mu^3),qquad P_{r_1}=P(mu),
]

and

[
oxed{P_{r_1}-P_{r_0}=rac{12}{193}(mu-mu^3)>0}
]

for every (0<mu<1).

Moreover,

[
P(
u)>3/4iff 
u>1/24.
]

Therefore, for

[
oxed{1/24<mule 24^{-1/3}},
]

the phase-discrimination task with success (>3/4) is available from output+branch sign and unavailable from the marginal-only record.

At (mu=1/10):

[
P_{r_0}=72131/96500approx0.7474715,
]

[
P_{r_1}=2909/3860approx0.7536269,
]

[
Delta P=297/48250approx0.00615544.
]

## Status

```text
HX_O_PASS = PASS
HX_A_PASS = PASS
HX_G_MODEL_PASS = PASS
UMI_INTERNAL_PASS = PASS
SC43_FULL_MATERIAL_PASS = HOLD
```

The useful UMI carrier is the **paired branch-sign/output relation**, not the sign bit in isolation.

The material gate is the next binding task: execute the branch-sign acquisition prospectively with frozen output pairing, phase reference, timing, losses, shuffling controls and resource accounting.
