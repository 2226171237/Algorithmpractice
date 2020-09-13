

def solve(nums,k):
    stack=[]
    for i in range(len(nums)):
        while len(stack) and nums[i]<stack[-1] and k>0:
            stack.pop()
            k-=1
        stack.append(nums[i])
    if k>0:
        stack=stack[:-k]
    i=0
    while i<len(stack) and stack[i]=='0':
        i+=1
    res=''.join(stack[i:]) if i<len(stack) else '0'
    return res

import sys
# nums=sys.stdin.readline().strip()
# k=int(sys.stdin.readline().strip())

print(solve('124356',2))
