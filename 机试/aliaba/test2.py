
import  sys

# n=int(sys.stdin.readline().strip())
# nums=sys.stdin.readline().strip().split(' ')
# nums=[int(x) for x in nums]

def getMaxId(C):
    i=0
    for j in range(len(C)):
        if C[i]<C[j]:
            i=j
    return i

def solve(n,C):
    G=[set() for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i!=j:
                G[i].add(j)
    Comp=[0]
    def dfs(u,com):
        if len(G[u])==0:
            Comp[0]=max(Comp[0],com)
            return
        for v in G[u]:
            G[u].remove(v)
            G[v].remove(u)
            dfs(v,com+C[u]*C[v])
            G[u].add(v)
            G[v].add(u)

    u=getMaxId(C)
    dfs(u,0)
    return Comp[0]

#print(solve(n,nums))

if __name__ == '__main__':
    print(solve(10,[1,2,3,4,5,6,7,8,9,10]))
