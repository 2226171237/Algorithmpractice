'''
在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。

示例:
输入:
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

输出: 4
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximal-square
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def maximalSquare(self, matrix):
        """
        动态规划 P(i,j) 以i,j为右下角的最大矩阵边长
        :type matrix: List[List[str]]
        :rtype: int
        """
        maxedge=0
        rows,cols=len(matrix),len(matrix[0])
        P=[[0 for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            if matrix[i][0]=='1':
                P[i][0]=1
                maxedge=1
        for i in range(cols):
            if matrix[0][i] == '1':
                P[0][i] = 1
                maxedge=1

        for i in range(1,rows):
            for j in range(1,cols):
                if matrix[i][j]=='1':
                    P[i][j]=min(P[i-1][j-1],P[i-1][j],P[i][j-1])+1
                    maxedge=max(maxedge,P[i][j])

        return maxedge**2

