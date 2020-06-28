'''
在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

示例:
现有矩阵 matrix 如下：
[  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]]
给定 target = 5，返回 true。
给定 target = 20，返回 false。
限制：
0 <= n <= 1000
0 <= m <= 1000
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution(object):
    def findNumberIn2DArray(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        M=len(matrix)
        if M==0:
            return False
        N=len(matrix[0])
        if N==0:
            return False
        def search(matrix,i,j,target):
            if i>=M or i<0:
                return False
            if j>=N or j<0:
                return False
            x=matrix[i][j]
            if x==target:
                return True
            elif x<target:
                return search(matrix,i+1,j,target)
            else:
                return search(matrix,i,j-1,target)
        return search(matrix,0,N-1,target)

    def findNumberIn2DArray2(self, matrix, target):
        M = len(matrix)
        if M == 0:
            return False
        N = len(matrix[0])
        if N == 0:
            return False
        i=0
        j=N-1
        while i<M and j>=0:
            x=matrix[i][j]
            if target>x:
                i+=1
            elif target<x:
                j-=1
            else:
                return True
        return False


if __name__ == '__main__':
    s=Solution()
    print(s.findNumberIn2DArray([[10]],5))
    print(s.findNumberIn2DArray2([[10]], 5))