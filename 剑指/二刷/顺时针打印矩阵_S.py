'''
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。

示例 1：
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
示例 2：
输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]

限制：
0 <= matrix.length <= 100
0 <= matrix[i].length <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shun-shi-zhen-da-yin-ju-zhen-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result=[]
        def printMatrix(i,j,rows,cols):
            if rows<=0 or cols<=0:
                return
            if rows==1:
                result.extend(matrix[i][j:j+cols])
                return
            if cols==1:
                for k in range(rows):
                    result.append(matrix[i+k][j])
                return
            result.extend(matrix[i][j:j+cols-1])
            for ii in range(i,i+rows-1):
                result.append(matrix[ii][j+cols-1])
            for jj in range(j+cols-1,j,-1):
                result.append(matrix[i+rows-1][jj])
            for ii in range(i+rows-1,i,-1):
                result.append(matrix[ii][j])
            printMatrix(i+1,j+1,rows-2,cols-2)
        rows=len(matrix)
        if rows==0:
            return []
        cols=len(matrix[0])
        printMatrix(0,0,rows,cols)
        return result

if __name__ == '__main__':
    s=Solution()
    print(s.spiralOrder([[1,2,3,4,5,6,7,8,9,10],[11,12,13,14,15,16,17,18,19,20]]))