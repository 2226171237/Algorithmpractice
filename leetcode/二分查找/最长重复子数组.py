'''
给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。

示例 1:
输入:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
输出: 3
解释:
长度最长的公共子数组是 [3, 2, 1]。
说明:
1 <= len(A), len(B) <= 1000
0 <= A[i], B[i] < 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def findLength(self, A, B):
        """
        dp[i][j] 定义为A[:i]和B[:j]的最长公共后缀长度
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        M,N=len(A),len(B)
        P=[[0 for _ in range(M)] for _ in range(N)]

        maxLen = 0
        for i in range(M):
            if A[i]==B[0]:
                P[i][0]=1
                maxLen=1
        for i in range(N):
            if A[0]==B[i]:
                P[0][i]=1
                maxLen = 1

        for i in range(1,M):
            for j in range(1,N):
                if A[i]==B[j]:
                    P[i][j]=P[i-1][j-1]+1
                    maxLen = max(maxLen,P[i][j])
        return maxLen


class SolutionQ(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = [0]
        marked = dict()

        def valid(row, col):
            for i in range(row):
                if marked[i] == col:
                    return False
                if abs(i - row) == abs(marked[i] - col):
                    return False
            return True
        P=[]
        def dfs(row):
            if row == n:
                result[0] += 1
                P.append(marked.copy())
                return
            for col in range(n):
                if valid(row, col):
                    marked[row] = col
                    dfs(row + 1)

        dfs(0)
        print(P)
        return result[0]

if __name__ == '__main__':
    s=SolutionQ()
    print(s.totalNQueens(4))
