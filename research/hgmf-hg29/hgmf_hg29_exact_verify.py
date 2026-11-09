#!/usr/bin/env python3
import math, importlib.util
from pathlib import Path
BASE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location("tests",BASE/"hgmf_hg29_tests.py")
m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
alpha=0.05/7
assert abs(alpha-1/140)<1e-15
assert abs(m.replication_p(0.001,0.006)-0.006)<1e-15
assert abs(m.nuisance_union_iut({"a":0.001,"b":0.004},["a","b"])["p_value"]-0.004)<1e-15
o=m.order_sign_test(8,0,0)
assert abs(o["p_value"]-1/256)<1e-15
o7=m.order_sign_test(7,0,0)
assert o7["p_value"]==1/128 and o7["p_value"]>alpha
assert o["p_value"]<alpha
assert abs(m.normal_sf(0)-0.5)<1e-15
print("PASS_HGMF_HG29_EXACT")
print(f"alpha_component={alpha}")
print("replication_combiner=max")
print("nuisance_union_combiner=max")
print("order_p_8_of_8=0.00390625")
print("order_p_7_of_7=0.0078125")
print("physical_protogeometry_confirmed=false")
