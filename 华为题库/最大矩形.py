'''
给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。

示例:
输入:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
输出: 6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximal-rectangle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def maximalRectangle(self, matrix) -> int:
        '''
        柱状图
        :param list[list[str]] matrix:
        :return: int
        '''
        if len(matrix)==0:
            return 0
        m,n=len(matrix),len(matrix[0])
        P=[[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1,m+1):
           for j in range(1,n+1):
                if matrix[i-1][j-1]=='1':
                    P[i][j]=P[i][j-1]+1

        # 可参考柱状图中最大矩形，来优化
        maxA = 0
        for i in range(1,m+1):
            for j in range(1,n+1):
                i_=i
                minW=P[i][j]
                while i_>=0:
                    if P[i_][j]==0:
                        break
                    else:
                        if minW>P[i_][j]:
                            minW=P[i_][j]
                        maxA=max(maxA,minW*(i-i_+1))
                    i_-=1
        return maxA





if __name__ == '__main__':
    S=Solution()
    matrix=[["1","0","1","0","0"],
            ["1","0","1","1","1"],
            ["1","1","1","1","1"],
            ["1","0","0","1","0"]
            ]
    print(S.maximalRectangle(matrix))



