'''
给定一个正整数 n，生成一个包含 1 到 n^2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。

示例:
输入: 3
输出:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/spiral-matrix-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res=[[0 for _ in range(n)] for _ in range(n)]
        sum=0
        def printMatrix(i,j,rows,cols):
            nonlocal sum
            if rows==0 or cols==0:
                return
            if rows==1:
                for jj in range(j,j+cols):
                    sum+=1
                    res[i][jj]=sum
                return
            if cols==1:
                for ii in range(i,i+rows):
                    sum+=1
                    res[ii][j]=sum
                    return
            for jj in range(j,j+cols-1):
                sum+=1
                res[i][jj]=sum
            for ii in range(i,i+rows-1):
                sum+=1
                res[ii][j+cols-1]=sum
            for jj in range(j+cols-1,j,-1):
                sum+=1
                res[i+rows-1][jj]=sum
            for ii in range(i+rows-1,i,-1):
                sum+=1
                res[ii][j]=sum
            printMatrix(i+1,j+1,rows-2,cols-2)
        printMatrix(0,0,n,n)
        return res

if __name__ == '__main__':
    s=Solution()
    res=s.generateMatrix(1)
    for x in res:
        print(x)
