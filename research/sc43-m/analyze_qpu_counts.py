#!/usr/bin/env python3
import argparse,json,math
from pathlib import Path

MU=.31
P1=(577+48*MU)/772
M0=1/(24*MU)
PS1=(1+MU**2)/2
PS0=(1+M0)/2

def b(s,i): return int(s[-1-i])
def reg2(s,h,l): return 2*b(s,h)+b(s,l)
def loglr(success,total,p1,p0):
    fail=total-success
    return success*math.log(p1/p0)+fail*math.log((1-p1)/(1-p0))

def main(path):
    data=json.loads(Path(path).read_text())
    sp=st=ec=et=mc=mt=raw=0
    for job in data['jobs']:
        arm=job['arm']; phase=int(job['phase']); target=(3*phase)%4
        for s,c in job['counts'].items():
            raw+=c
            A=reg2(s,0,1); B=reg2(s,2,3)
            sign=b(s,4); filt=b(s,5); mainv=reg2(s,6,7)
            pa=(A==3 and B<3) or (B==3 and A<3)
            if pa:
                st+=c
                if sign==0: sp+=c
            if pa and filt==0:
                if arm=='enriched':
                    et+=c; ec+=c*(mainv==target)
                else:
                    mt+=c; mc+=c*(mainv==target)
    lp=loglr(ec,et,P1,.75) if et else float('-inf')
    ls=loglr(sp,st,PS1,PS0) if st else float('-inf')
    print(json.dumps({
      'raw_shots':raw,
      'enriched_rate':ec/et if et else None,
      'marginal_rate':mc/mt if mt else None,
      'sign_mean':2*sp/st-1 if st else None,
      'e_phase':math.exp(lp) if lp<700 else float('inf'),
      'e_sign':math.exp(ls) if ls<700 else float('inf'),
      'joint_pass':lp>=math.log(40) and ls>=math.log(40)
    },indent=2))

if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('counts_json'); main(ap.parse_args().counts_json)
