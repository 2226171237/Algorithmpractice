'''
给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。
一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。
你可以假设网格的四个边均被水包围。

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

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-islands
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def numIslands(self, grid) -> int:
        '''
        DFS 无向图遍历
        :param list[list[str]] grid:
        :return:
        '''
        if len(grid)==0:
            return 0
        m,n=len(grid),len(grid[0])
        visited=[[False for _ in range(n)] for _ in range(m)]
        island=0

        def isValid(i,j):
            return 0<=i<m and 0<=j<n

        def _dfs(grid,visited,i,j):
            visited[i][j]=True
            if isValid(i,j-1) and grid[i][j-1]=='1' and not visited[i][j-1]:
                _dfs(grid,visited,i,j-1)
            if isValid(i,j+1) and grid[i][j+1]=='1' and not visited[i][j+1]:
                _dfs(grid,visited,i,j+1)
            if isValid(i-1,j) and grid[i-1][j]=='1' and not visited[i-1][j]:
                _dfs(grid,visited,i-1,j)
            if isValid(i+1,j) and grid[i+1][j]=='1' and not visited[i+1][j]:
                _dfs(grid,visited,i+1,j)

        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j]=='1':
                    island+=1
                    _dfs(grid,visited,i,j)
        return island

if __name__ == '__main__':
    S=Solution()
    grid=[["1","1","1"],
          ["0","1","0"],
          ["1","1","1"]]
    print(S.numIslands(grid))


