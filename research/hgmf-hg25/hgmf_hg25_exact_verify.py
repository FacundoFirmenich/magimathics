#!/usr/bin/env python3
import math
fields=[100,150,200]
cycles=range(1,9)
waves=range(1,4)
full_cells=len(fields)*len(list(cycles))*len(list(waves))
assert full_cells==72
full_rectangles=(len(fields)-1)*(8-1)*3
assert full_rectangles==42
def staged(f,c):
    return (f in (100,150) and c<=5) or f==200
staged_cells=sum(staged(f,c) for w in waves for f in fields for c in range(1,9))
assert staged_cells==54
missing_cells=72-staged_cells
assert missing_cells==18
staged_rect=0
for w in waves:
    for f0,f1 in zip(fields[:-1],fields[1:]):
        for c0 in range(1,8):
            corners=[(f0,c0),(f0,c0+1),(f1,c0),(f1,c0+1)]
            staged_rect += all(staged(f,c) for f,c in corners)
assert staged_rect==24
assert full_rectangles-staged_rect==18
z=1.959963984540054+0.8416212335729143
assert abs(z*2/math.sqrt(2)-3.9620398115993454)<1e-12
assert abs(z*2/math.sqrt(3)-3.2349919596703978)<1e-12
print("PASS_HGMF_HG25_EXACT")
print("magnetic_full_grid_loops=72")
print("full_adjacent_rectangles=42")
print("conditional_staged_loops=54")
print("conditional_missing_loops=18")
print("conditional_staged_rectangles=24")
print("conditional_missing_rectangles=18")
print("certified_executed_target_grid_loops=0")
print("adsorption_homologous_runs_executed=0")
print("empirical_verdict=ABSTAIN_INSUFFICIENT_EXECUTION")
