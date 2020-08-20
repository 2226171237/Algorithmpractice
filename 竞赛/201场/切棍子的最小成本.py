

class Solution(object):
    def minCost(self, n, cuts):
        """

        dp[L][R] 表示做端点为L，右端点为R的最小损失，L,R 只可能为0，n 或cuts中的数
        :type n: int
        :type cuts: List[int]
        :rtype: int
        """
        dp=[[-1 for _ in range(103)] for _ in range(103)]
        def dfs(l,r,n,cuts):
            if dp[l][r]!=-1:
                return dp[l][r]
            if l+1==r:
                dp[l][r]=0
                return 0
            minCost=2**31
            for i in range(l+1,r):
                minCost= min(dfs(l,i,n,cuts)+dfs(i,r,n,cuts)+cuts[r]-cuts[l],minCost)
            dp[l][r]=minCost
            return minCost

        cuts.append(0)
        cuts.append(n)
        return dfs(0,len(cuts)-1,n,sorted(cuts))



