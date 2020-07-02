'''
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。
此外，你可以假设该网格的四条边均被水包围。

示例 1:
输入:
    11110
    11010
    11000
    00000
输出: 1
示例 2:
输入:
    11000
    11000
    00100
    00011
输出: 3
解释: 每座岛屿只能由水平和/或竖直方向上相邻的陆地连接而成。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-islands
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid)==0:
            return 0
        M,N=len(grid),len(grid[0])
        marked=[[False for _ in range(N)] for _ in range(M)]

        def valid(grid,i,j):
            return 0<=i<M and 0<=j<N and marked[i][j]==False  and grid[i][j]=='1'

        def dfs(grid,i,j):
            if not valid(grid,i,j):
                return
            marked[i][j]=True
            dfs(grid,i+1,j)
            dfs(grid, i - 1, j)
            dfs(grid,i,j+1)
            dfs(grid,i,j-1)

        res=0
        for i in range(M):
            for j in range(N):
                if valid(grid,i,j):
                    dfs(grid,i,j)
                    res+=1
        return res

if __name__ == '__main__':
    s=Solution()
    print(s.numIslands([['1','1','1','1','0'],['1','1','0','1','0'],['1','1','0','0','0'],['0','0','0','0','0']]))