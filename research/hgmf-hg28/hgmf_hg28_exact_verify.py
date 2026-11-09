#!/usr/bin/env python3
alpha=0.05
J=7
a=alpha/J
assert abs(a-1/140)<1e-15
assert 2**-7 > a
assert 2**-8 < a
n=min(k for k in range(1,30) if 2**(-k)<=a)
assert n==8
base=144
train=3*2*2
hold=8*2*2
assert train==12
assert hold==32
assert base+train+hold==188
assert 288-188==100
print("PASS_HGMF_HG28_EXACT")
print(f"alpha_component={a}")
print("min_holdout_order_pairs_one_sided=8")
print(f"min_p_n7={2**-7}")
print(f"min_p_n8={2**-8}")
print("order_training_units=12")
print("order_holdout_units=32")
print("sparse_total_max=188")
print("savings_vs_full_reverse=100")
print("strong_FWER_bound=0.05")
print("empirical_confirmation=false")
