

import sys

def solve(s):
    if 0==len(s) or len(s)>10:
        return False
    for x in s:
        if ord('a')<=ord(x)<=ord('z') or ord('A')<=ord(x)<=ord('Z'):
            continue
        else:
            return False
    return True


T=int(sys.stdin.readline().strip())
cnt=0
for _ in range(T):
    s=sys.stdin.readline().strip()
    if solve(s):
        cnt+=1
print(cnt)

