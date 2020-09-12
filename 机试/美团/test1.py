

import sys
sys.stdin.readline()
def solve(p,q):
    p=set(p)
    q=set(q)
    a=set(p)-set(q)
    b=set(q)-set(p)
    c=set(p)& set(q)
    return [len(a),len(b),len(c)]
p=[int(x) for x in sys.stdin.readline().strip().split(' ')]
q=[int(x) for x in sys.stdin.readline().strip().split(' ')]

result=solve(p,q)
print(' '.join(map(str,result)))
