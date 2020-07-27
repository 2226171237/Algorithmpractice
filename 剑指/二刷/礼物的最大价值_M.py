'''
在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。
你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。
给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？

示例 1:
输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 12
解释: 路径 1→3→5→2→1 可以拿到最多价值的礼物
 
提示：
0 < grid.length <= 200
0 < grid[0].length <= 200
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/li-wu-de-zui-da-jie-zhi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def maxValue(self, grid):
        """
        DFS 超时
        :type grid: List[List[int]]
        :rtype: int
        """
        rows=len(grid)
        if rows==0:
            return 0
        cols=len(grid[0])
        max_gift_nums=rows+cols-1
        max_gift_value=[0]
        def isValid(i,j):
            return 0<=i<rows and 0<=j<cols

        def dfs(i,j,gift_num,gift_value):
            if gift_num==max_gift_nums:
                max_gift_value[0]=max(max_gift_value[0],gift_value)
                return
            if isValid(i,j+1):
                dfs(i,j+1,gift_num+1,gift_value+grid[i][j+1])
            if isValid(i+1,j):
                dfs(i+1, j, gift_num + 1, gift_value + grid[i+1][j])
        dfs(0,0,1,grid[0][0])
        return max_gift_value[0]

    def maxValue2(self, grid):
        '''
        动态规划
        :param grid:
        :return:
        '''
        rows = len(grid)
        if rows == 0:
            return 0
        cols = len(grid[0])
        P=[[0 for _ in range(cols)] for _ in range(rows)]
        P[0][0]=grid[0][0]
        for j in range(1,cols):
            P[0][j]=P[0][j-1]+grid[0][j]
        for i in range(1,rows):
            P[i][0]=P[i-1][0]+grid[i][0]

        for i in range(1,rows):
            for j in range(1,cols):
                P[i][j]=max(P[i-1][j],P[i][j-1])+grid[i][j]

        return P[-1][-1]

if __name__ == '__main__':
    s=Solution()
    print(s.maxValue([[1,3,1],[1,5,1],[4,2,1]]))
    print(s.maxValue2([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
