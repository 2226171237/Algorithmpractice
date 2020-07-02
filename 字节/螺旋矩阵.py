'''
给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。

示例 1:
输入:
[ [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]]
输出: [1,2,3,6,9,8,7,4,5]
示例 2:
输入:
[  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]]
输出: [1,2,3,4,8,12,11,10,9,5,6,7]
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/spiral-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res=[]
        if len(matrix)==0:
            return []
        rows,cols=len(matrix),len(matrix[0])
        def printMatrix(matrix,i,j,rows,cols):
            if rows<=0 or cols<=0:
                return
            if rows==1:
                res.extend(matrix[i][j:j+cols])
                return
            if cols==1:
                for ii in range(i,i+rows):
                    res.append(matrix[ii][j])
                return
            for jj in range(j,j+cols):
                res.append(matrix[i][jj])
            for ii in range(i+1,i+rows):
                res.append(matrix[ii][j+cols-1])
            for jj in range(j+cols-2,j-1,-1):
                res.append(matrix[i+rows-1][jj])
            for ii in range(i+rows-2,i,-1):
                res.append(matrix[ii][j])

            printMatrix(matrix,i+1,j+1,rows-2,cols-2)

        printMatrix(matrix,0,0,rows,cols)
        return res

if __name__ == '__main__':
    s=Solution()
    print(s.spiralOrder([ [1, 2, 3],
                          [5, 6, 7],
                          [9,10,11],
                          [9,10,11]]))