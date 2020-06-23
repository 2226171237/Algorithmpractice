'''
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。
一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），
也不能进入行坐标和列坐标的数位之和大于k的格子。
例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。
但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？

示例 1：
输入：m = 2, n = 3, k = 1
输出：3

示例 2：
输入：m = 3, n = 1, k = 0
输出：1

提示：
1 <= n,m <= 100
0 <= k <= 20
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def movingCount(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        result=[0]
        marked=[[False for _ in range(n)] for _ in range(m)]
        def getnum(i,j):
            s=0
            for x in str(i):
                s+=int(x)
            for x in str(j):
                s+=int(x)
            return s
        def valid(m,n,i,j,k):
            return 0<=i<m and 0<=j<n and marked[i][j]==False and getnum(i,j)<=k

        def dfs(i,j):
            marked[i][j]=True
            result[0]+=1
            if valid(m,n,i,j+1,k):
                dfs(i,j+1)
            if valid(m,n,i,j-1,k):
                dfs(i,j-1)
            if valid(m,n,i-1,j,k):
                dfs(i-1,j)
            if valid(m,n,i+1,j,k):
                dfs(i+1,j)
        dfs(0,0)
        return result[0]

if __name__ == '__main__':
    s=Solution()
    print(s.movingCount(3,1,0))
