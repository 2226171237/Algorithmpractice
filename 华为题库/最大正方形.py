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
class Solution:
    def maximalSquare(self, matrix: list) -> int:
        '''
        动态规划，P(i,j)表示以i,j为正方形右下角的最大边长。
        P(i,j)=min(P(i,j-1),P(i-1,j-1),P(i-1,j))+1,左边，左上角，正上方 三个方格
        :param matrix:
        :return:
        '''
        if len(matrix)==0:
            return 0
        m, n = len(matrix), len(matrix[0])
        P=[[0 for _ in range(n)] for _ in range(m)]
        i=0
        maxLen = 0
        while i<m:
            if matrix[i][0]=='1':
                P[i][0]=1
                maxLen = 1
            i+=1
        i=0
        while i<n:
            if matrix[0][i]=='1':
                P[0][i]=1
                maxLen = 1
            i+=1

        for j in range(1,n):
            for i in range(1,m):
                if matrix[i][j]=='1':
                    P[i][j]=min(P[i][j-1],P[i-1][j-1],P[i-1][j])+1
                    maxLen=max(maxLen,P[i][j])
        return maxLen**2



if __name__ == '__main__':
    L=[["1","0","1","0","0"],
       ["1","0","1","1","1"],
       ["1","1","1","1","1"],
       ["1","0","0","1","0"]]
    S=Solution()
    print(S.maximalSquare(L))



