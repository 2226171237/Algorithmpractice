'''
给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。

例如，给定三角形：
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/triangle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        minSum=[2**31]
        def dfs(layer,i,sum):
            if layer==len(triangle):
                minSum[0]=min(minSum[0],sum)
                return
            if i>=len(triangle[layer]):
                return
            x=triangle[layer][i]
            dfs(layer+1,i,sum+x)
            dfs(layer+1,i+1,sum+x)
        dfs(0,0,0)
        return minSum[0]

    def minimumTotal2(self, triangle):
        dp=[x.copy() for x in triangle]
        layers=len(triangle)
        for layer in range(1,layers):
            dp[layer][0]=dp[layer-1][0]+triangle[layer][0]
            dp[layer][-1]=dp[layer-1][-1]+triangle[layer][-1]
            for i in range(1,len(triangle[layer])-1):
                dp[layer][i]=min(dp[layer-1][i-1],dp[layer-1][i])+triangle[layer][i]
        return min(dp[-1])

if __name__ == '__main__':
    S=Solution()
    print(S.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))
    print(S.minimumTotal2([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))