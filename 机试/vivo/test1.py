
def solve2(grids,s,d):
    if grids[s[0]][s[1]] in '#@':
        return -1
    if grids[d[0]][d[1]] in '#@':
        return -1
    m,n=len(grids),len(grids[0])
    marked=[[False for _ in range(n)] for _ in range(m)]
    minD=[2**31]
    def isValid(i,j):
        return 0<=i<m and 0<=j<n and not marked[i][j] and grids[i][j] not in '#@'
    def dfs(i,j,times):
        if not isValid(i,j):
            return
        if (i,j)==d:
            minD[0]=min(minD[0],times)
            return
        marked[i][j]=True
        dfs(i+1,j,times+1)
        dfs(i-1,j,times+1)
        dfs(i,j+1,times+1)
        dfs(i,j-1,times+1)
        marked[i][j]=False
    dfs(s[0],s[1],0)
    return minD[0]

from collections import deque
def solve(grids,s,d):
    if grids[s[0]][s[1]] in '#@':
        return -1
    if grids[d[0]][d[1]] in '#@':
        return -1
    m,n=len(grids),len(grids[0])
    marked=[[False for _ in range(n)] for _ in range(m)]
    dist=[[0,1],[0,-1],[-1,0],[1,0]]
    Q=deque()
    Q.append(s)
    marked[s[0]][s[1]]=True
    steps=0
    while len(Q):
        sz=len(Q)
        for _ in range(sz):
            node=Q.popleft()
            if node==d:
                return steps
            for k in range(4):
                i=node[0]+dist[k][0]
                j=node[1]+dist[k][1]
                if 0<=i<m and 0<=j<n and not marked[i][j] and grids[i][j] not in '#@':
                    Q.append((i,j))
                    marked[i][j] = True
        steps+=1
    return -1


import sys
n=int(sys.stdin.readline().strip())
points=[int(x) for x in sys.stdin.readline().strip().split(' ')]
s=(points[0],points[1])
d=(points[2],points[3])
grids=[]
for _ in range(n):
    grids.append(sys.stdin.readline().strip())
print(solve(grids,s,d))

