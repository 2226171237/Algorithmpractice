

def solve(s1,s2):
    result=[]
    def index(s,a):
        for i in range(len(s)):
            if s[i]==a:
                return i
        return -1
    def preOrder(s1,s2):
        if len(s1)==0:
            return
        root=s2[-1]
        result.append(root)
        i=index(s1,root)
        left=s1[:i]
        right=s1[i+1:]
        preOrder(left,s2[:i])
        preOrder(right,s2[i:-1])
    preOrder(s1,s2)
    return ''.join(result)

import sys
s1,s2=sys.stdin.readline().strip().split(' ')
print(solve(s1,s2))
