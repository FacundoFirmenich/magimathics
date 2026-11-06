import math

def qasm(mu=0.31,n=0,enriched=True):
    th_h=2*math.asin(math.sqrt(5/13))
    alpha0=math.pi/2
    alpha1=2*math.asin(1/math.sqrt(5))
    delta=alpha1-alpha0
    th_e=2*math.acos(mu)
    th_f=2*math.acos(1/4)
    L=['OPENQASM 2.0;','include "qelib1.inc";',
       'gate mycry(theta) c,t { ry(theta/2) t; cx c,t; ry(-theta/2) t; cx c,t; }',
       'qreg q[12];','creg c[8];']
    def prep(h,l,e):
        L.extend([f'ry({th_h:.17g}) q[{h}];',
                  f'ry({alpha0:.17g}) q[{l}];',
                  f'mycry({delta:.17g}) q[{h}],q[{l}];',
                  f'ccx q[{h}],q[{l}],q[11];',
                  f'mycry({th_e:.17g}) q[11],q[{e}];',
                  f'ccx q[{h}],q[{l}],q[11];'])
        for _ in range(n%4):
            L.extend([f'z q[{h}];',f's q[{l}];'])
    prep(0,1,2); prep(3,4,5); prep(6,7,8)
    L.append('h q[9];')
    for a,b in [(0,3),(1,4)]:
        L.extend([f'cx q[{b}],q[{a}];',f'ccx q[9],q[{a}],q[{b}];',f'cx q[{b}],q[{a}];'])
    L.extend(['h q[9];','ccx q[6],q[7],q[11];',
              f'mycry({th_f:.17g}) q[11],q[10];',
              'ccx q[6],q[7],q[11];',
              'x q[7]; cx q[7],q[6]; x q[7];',
              'h q[7]; ccx q[9],q[6],q[7]; h q[7];'])
    if enriched:
        L.append('h q[7]; ccx q[9],q[6],q[7]; h q[7];')
    L.extend(['cx q[6],q[7]; cx q[7],q[6]; cx q[6],q[7];',
              'h q[7];','cu1(-pi/2) q[6],q[7];','h q[6];'])
    for qi,ci in [(0,0),(1,1),(3,2),(4,3),(9,4),(10,5),(6,6),(7,7)]:
        L.append(f'measure q[{qi}] -> c[{ci}];')
    return '\n'.join(L)+'\n'

if __name__=='__main__':
    for n in range(4):
        for enriched in (False,True):
            arm='enriched' if enriched else 'marginal'
            open(f'hx_q4_mu0p31_n{n}_{arm}.qasm','w').write(qasm(.31,n,enriched))
