'''
在二维地图上， 0代表海洋， 1代表陆地，我们最多只能将一格 0 海洋变成 1变成陆地。
进行填海之后，地图上最大的岛屿面积是多少？（上、下、左、右四个方向相连的 1 可形成岛屿）

示例 1:
输入: [[1, 0], [0, 1]]
输出: 3
解释: 将一格0变成1，最终连通两个小岛得到面积为 3 的岛屿。
示例 2:
输入: [[1, 1], [1, 0]]
输出: 4
解释: 将一格0变成1，岛屿的面积扩大为 4。
示例 3:
输入: [[1, 1], [1, 1]]
输出: 4
解释: 没有0可以让我们变成1，面积依然为 4。
说明:
1 <= grid.length = grid[0].length <= 50
0 <= grid[i][j] <= 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/making-a-large-island
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Union:
    def __init__(self,N):
        self.arrs=[i for i in range(N)]
        self.size={i:1 for i in range(N)}
        self._counts=N

    def find(self,p):
        while self.arrs[p]!=p:
            p=self.arrs[p]
        return p

    def componetSize(self,p):
        cnt=1
        while self.arrs[p]!=p:
            p=self.arrs[p]
            cnt+=1
        return cnt

    def union(self,p,q):
        p_id=self.find(p)
        q_id=self.find(q)
        if p_id==q_id:
            return
        else:
            self.arrs[q_id]=p_id
            self.size[p_id]+=self.size[q_id]
            self._counts-=1

class Solution(object):
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows=len(grid)
        cols=len(grid[0])

        def isValid(i,j,marked):
            return i>=0 and i<rows and j>=0 and j<cols and grid[i][j]==1 and marked[i][j]==False

        area=[0]
        def dfs(i,j,marked):
            if not isValid(i,j,marked):
                return
            marked[i][j]=True
            area[0]+=1
            dfs(i-1,j,marked)
            dfs(i+1,j,marked)
            dfs(i,j-1,marked)
            dfs(i,j+1,marked)

        maxA=0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==0:
                    area[0]=0
                    grid[i][j]=1
                    marked = [[False for _ in range(cols)] for _ in range(rows)]
                    dfs(i,j,marked)
                    grid[i][j]=0
                    maxA=max(maxA,area[0])

        return maxA if area[0]>0 else cols*rows

    def largestIsland2(self, grid):
        '''union find'''
        rows = len(grid)
        cols = len(grid[0])
        UF=Union(rows*cols)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    if 0<=i+1<rows and grid[i][j]==grid[i+1][j]:
                        UF.union(i*cols+j,(i+1)*cols+j)
                    if 0<=j+1<cols and grid[i][j]==grid[i][j+1]:
                        UF.union(i*cols+j,i*cols+j+1)
        maxA=0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    area=0
                    com=set()
                    if 0<=i-1<rows and  grid[i-1][j]==1:
                        com.add(UF.find((i-1)*cols+j))
                    if 0<=i+1<rows and grid[i+1][j]==1:
                        com.add(UF.find((i+1)*cols+j))
                    if 0<=j-1<cols and grid[i][j-1]==1:
                        com.add(UF.find(i*cols+j-1))
                    if 0<=j+1<cols and grid[i][j+1]==1:
                        com.add(UF.find(i*cols+j+1))
                    for p in com:
                        area+=UF.size[p]
                    area+=1
                    maxA=max(maxA,area)
        return maxA if maxA>0 else cols*rows




if __name__ == '__main__':
    s=Solution()
    print(s.largestIsland2([[1,0],[1,1]]))