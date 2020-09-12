

from functools import lru_cache
def solve(dist,N,M):
    @lru_cache(10000)
    def dfs(s,t):
        if s<=0:
            return t-1
        if t>N:
            return 2**31
        res=2**31
        d=0
        for i in range(3):
            if t+i>=N:
                break
            d+=dist[t+i]
            res=min(res,dfs(s-d,t+i+2))
        return res
    t=dfs(M,0)
    return -1 if t==2**31 else t

# import sys
# M=int(sys.stdin.readline().strip())
# N=int(sys.stdin.readline().strip())
# dist=[]
# for _ in range(N):
#     dist.append(int(sys.stdin.readline().strip()))
#
# print(solve(dist,N,M))

print(solve([2,3,4,2,3,4],6,10))



