class UF:
    def __init__(self,N):
        self.ids=list(range(N))
        self._counts=N

    def union(self,p,q):
        pRoot=self.find(p)
        qRoot=self.find(q)
        if pRoot==qRoot:
            return
        self.ids[qRoot]=pRoot
        self._counts-=1

    def find(self,p):
        while self.ids[p]!=p:
            p=self.ids[p]
        return p

    def connect(self,p,q):
        pRoot=self.find(p)
        qRoot=self.find(q)
        return pRoot==qRoot

    def __len__(self):
        return self._counts

class Solution(object):
    def numIslands1(self, grid):
        """
        使用交并集
        :type grid: List[List[str]]
        :rtype: int
        """
        m=len(grid)
        if m==0:
            return 0
        n=len(grid[0])
        N=m*n
        uf=UF(N)
        zeros_num=0
        dist=[[0,1],[0,-1],[1,0],[-1,0]]
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='0':
                    zeros_num+=1
                else:
                    id=i*n+j
                    for k in range(4):
                        neg_i=i+dist[k][0]
                        neg_j=j+dist[k][1]
                        neg_id=neg_i*n+neg_j
                        if 0<=neg_i<m and 0<=neg_j<n and grid[neg_i][neg_j]=='1':
                            uf.union(id,neg_id)
        return len(uf)-zeros_num

    def numIslands2(self,grid):
        '''
        使用dfs
        :param grid:
        :return:
        '''
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        marked=[[False for _ in range(n)] for _ in range(m)]
        def isValid(i,j):
            return 0<=i<m and 0<=j<n and grid[i][j]=='1' and marked[i][j]==False

        def dfs(i,j):
            if not isValid(i,j):
                return
            marked[i][j]=True
            dfs(i,j-1)
            dfs(i,j+1)
            dfs(i-1,j)
            dfs(i+1,j)
        cnt=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1' and not marked[i][j]:
                    dfs(i,j)
                    cnt+=1
        return cnt
