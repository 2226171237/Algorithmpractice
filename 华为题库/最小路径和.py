'''
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
说明：每次只能向下或者向右移动一步。

示例:
输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。
'''

class Solution:
    def minPathSum(self, grid) -> int:
        '''
        动态规划
        :param list[list[int]] grid:
        :return:
        '''
        m,n=len(grid),len(grid[0])
        P=[[0 for _ in range(n)] for _ in range(m)]
        P[0][0]=grid[0][0]
        for i in range(1,n):
            P[0][i]=P[0][i-1]+grid[0][i]
        for i in range(1,m):
            P[i][0]=P[i-1][0]+grid[i][0]

        for i in range(1,m):
            for j in range(1,n):
                P[i][j]=min(P[i-1][j],P[i][j-1])+grid[i][j]

        return P[-1][-1]

if __name__ == '__main__':
    S=Solution()
    grid=[[1,3,1],
          [1,5,1],
          [4,2,1]]
    print(S.minPathSum(grid=grid))
