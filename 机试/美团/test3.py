

def solve(a):
    n=len(a)
    result=0

    prev=[0 for _ in range(n)]
    for i in range(1,n):
        prev[i]=prev[i-1]^i

    for i in range(1,n+1):
        result^=a[i-1]
        c=n//i
        t = n % i
        if c%2==1:
            result^=prev[i-1]
        result^=prev[t]
    return result

for i in range(1,10):
    for j in range(1,10):
        print(i%j,end=' ')
    print()

import sys
n=sys.stdin.readline()
a=[int(x) for x in sys.stdin.readline().strip().split(' ')]
print(solve(a))