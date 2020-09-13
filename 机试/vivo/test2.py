


def isHuiwen(s):
    i=0
    j=len(s)-1
    while i<j and s[i]==s[j]:
        i+=1
        j-=1
    return i==j

def solve(s):
    if isHuiwen(s):
        return s
    for i in range(len(s)):
        t=s[:i]+s[i+1:]
        if isHuiwen(t):
            return t
    return 'false'

# import sys
# s=sys.stdin.readline().strip()
print(solve('abcba'))

