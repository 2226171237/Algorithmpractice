
def solve(dist,L,T,X):
    dist=set(dist)
    mem=dict()
    def dfs(p,t):
        if (p,t) in mem:
            return mem[(p,t)]
        if p in dist:
            t+=1
        if p>=X:
            return t
        res=2**31
        for x in range(L,T+1):
            res=min(res,dfs(p+x,t))
        mem[(p,t)]=res
        return res
    return dfs(0,0)

# import sys
# X=int(sys.stdin.readline().strip())
# L,T,N=[int(x) for x in sys.stdin.readline().strip().split(' ')]
# dist=[int(x) for x in sys.stdin.readline().strip().split(' ')]
# print(solve(dist,L,T,X))


