'''

'''

import sys

K=int(sys.stdin.readline().strip())
N=int(sys.stdin.readline().strip())
R=int(sys.stdin.readline().strip())

class Node:
    def __init__(self,id):
        self.id=id
        self.childs=[]
        self.lengths=[]
        self.cost=[]

class Graph:
    def __init__(self,N):
        self.V=[Node(x) for x in range(1,N+1)]

    def buildGraph(self,S,D,L,T):
        self.V[S-1].childs.append(D)
        self.V[S-1].lengths.append(L)
        self.V[S-1].cost.append(T)

G=Graph(N)
for _ in range(R):
    line=sys.stdin.readline().strip().split()
    line=list(map(int,line))
    G.buildGraph(*line)

def DFS(G:Graph,maxCost:int,N):
    '''最大成本条件下，找到最短路径长度'''
    minLens=[2**31]
    visited=[False for _ in range(N)]
    def dfs(v,lens:int,cost):
        if cost>maxCost:
            return
        if v==N and cost<=maxCost:
            minLens[0]=min(minLens[0],lens)
            return
        visited[v-1]=True
        for i,u in enumerate(G.V[v-1].childs):
            if visited[u-1]==False:
                dfs(u,lens+G.V[v-1].lengths[i],cost+G.V[v-1].cost[i])
        visited[v - 1] = False

    dfs(1,0,0)
    return -1 if minLens[0]==2**31 else minLens[0]

print(DFS(G,K,N))


'''
5  K  maxCost
6  N
7  R
1 2 2 4
2 4 3 3
3 4 2 4
1 3 4 1
4 6 2 1
3 5 2 0
5 4 3 1
'''
