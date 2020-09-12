

def solve1(s1,s2):
    s1=s1.lower()
    s2=s2.lower()
    n1=len(s1)
    n2=len(s2)
    if n1<n2:
        s_t = s2[n1:]
        s2=s2[:n1]
    else:
        s_t = s1[n2:]
        s1=s1[:n2]
    n=len(s1)
    if s1!=s2:
        return ''
    patten=''
    for i in range(1,n+1):
        if n%i==0:
            c1=n//i
            c2=len(s_t)//i
            if s1[:i]*c1==s1 and s1[:i]*c2==s_t:
                patten=s1[:i]
    return patten

import sys
# s1=sys.stdin.readline().strip()
# s2=sys.stdin.readline().strip()
print(solve1('abcdabcdabcdabcd','abcdabcdabcd'))





