'''
你现在手里有一份大小为 N x N 的「地图」（网格） grid，上面的每个「区域」（单元格）都用 0 和 1 标记好了。
其中 0 代表海洋，1 代表陆地，请你找出一个海洋区域，这个海洋区域到离它最近的陆地区域的距离是最大的。

我们这里说的距离是「曼哈顿距离」（ Manhattan Distance）：(x0, y0) 和 (x1, y1) 这两个区域之间的距离是 |x0 - x1| + |y0 - y1| 。
如果我们的地图上只有陆地或者海洋，请返回 -1。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/as-far-from-land-as-possible
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

from collections import deque
class Solution:
    def maxDistance(self, grid) -> int:
        '''
        BFS,超时
        :param list[list[int]] grid:
        :return:
        '''
        m,n=len(grid),len(grid[0])

        def bfs(grid,i,j,visited):
            Q=deque()
            Q.append((i,j))
            while len(Q):
                i1,j1=Q.popleft()
                if grid[i1][j1]==1:
                    return abs(i1-i)+abs(j1-j)
                visited[i1][j1]=1
                if 0<=j1-1<n and visited[i1][j1-1]==0:
                    Q.append((i1,j1-1))
                if 0<=i1-1<m and visited[i1-1][j1]==0:
                    Q.append((i1-1,j1))
                if 0<=i1+1<n and visited[i1+1][j1]==0:
                    Q.append((i1+1,j1))
                if 0<=j1+1<n and visited[i1][j1+1]==0:
                    Q.append((i1,j1+1))
            return -1
        maxD=-1
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    visited = [[0 for _ in range(n)] for _ in range(m)]
                    maxD=max(maxD,bfs(grid,i,j,visited))
        return maxD
    def maxDistance2(self, grid) -> int:
        '''
        多源BFS，其实就是有一个超级原点，然后从该点进行BFS遍历，多源点是超级原点的邻接点。
        :param grid:
        :return:
        '''
        m,n=len(grid),len(grid[0])
        Q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    Q.append((i,j,0))

        maxLens=-1
        hasOcean=False
        while len(Q):
            i1,j1,d=Q.popleft()
            if grid[i1][j1]==0:
                maxLens=max(maxLens,d)
            grid[i1][j1]+=1 # 代替访问标志
            if 0<=j1-1<n and grid[i1][j1-1]==0:
                Q.append((i1,j1-1,d+1))
                hasOcean=True
            if 0<=i1-1<m and grid[i1-1][j1]==0:
                Q.append((i1-1,j1,d+1))
                hasOcean = True
            if 0<=i1+1<n and grid[i1+1][j1]==0:
                Q.append((i1+1,j1,d+1))
                hasOcean = True
            if 0<=j1+1<n and grid[i1][j1+1]==0:
                Q.append((i1,j1+1,d+1))
                hasOcean = True
        if hasOcean:
            return maxLens
        else:
            return -1

if __name__ == '__main__':
    S=Solution()
    grid=[[1,0,1],[0,0,0],[1,0,1]]
    print(S.maxDistance(grid))
    print(S.maxDistance2(grid))


