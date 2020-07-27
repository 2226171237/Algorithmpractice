# 问题1：
# 股票的最大利润：
# 假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？
# 示例 1:
# 输入: [7,1,5,3,6,4]
# 输出: 5
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
#      注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
# 示例 2:
# 输入: [7,6,4,3,1]
# 输出: 0
# 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

# k=1 次 即只能买卖一次
class Solution1(object):
    def maxProfit(self, prices):
        """
        DP[n,{0,1}],第n天，状态：0：没有，1：持有
        DP表示当前手里的钱
        :type prices: List[int]
        :rtype: int
        """
        N=len(prices)
        if N==0:
            return 0
        dp=[[0,0] for _ in range(N)]
        dp[0][0]=0
        dp[0][1]=-prices[0]
        for i in range(1,N):
            dp[i][0]=max(dp[i-1][1]+prices[i],dp[i-1][0])
            dp[i][1]=max(-prices[i],dp[i-1][1])  # 之前没有买卖，所以之前手里的钱就是0
        return dp[-1][0]

# k=infinity,可以买卖无穷次
class Solution2(object):
    def maxProfit(self, prices):
        """
        DP[n,{0,1}],第n天，可用操作数为k，状态：0：没有，1：持有
        DP表示当前手里的钱
        :type prices: List[int]
        :rtype: int
        """
        N=len(prices)
        if N==0:
            return 0
        dp=[[0,0] for _ in range(N)]
        dp[0][0]=0
        dp[0][1]=-prices[0]
        for i in range(1,N):
            dp[i][0]=max(dp[i-1][1]+prices[i],dp[i-1][0])
            dp[i][1]=max(dp[i-1][0]-prices[i],dp[i-1][1])
        return dp[-1][0]


# 给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
# 设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。
# k=2
class Solution3(object):
    def maxProfit(self, prices):
        """
        DP[n,k,{0,1}],第n天，可用操作数为k，状态：0：没有，1：持有
        DP表示当前手里的钱
        :type prices: List[int]
        :rtype: int
        """
        N=len(prices)
        if N==0:
            return 0
        dp=[[[0,0] for _ in range(3)] for _ in range(N+1)]
        # 还没有股票可买卖
        for k in range(3):
            dp[0][k][0]=0
            dp[0][k][1]=-2**31
        # 没有操作可执行
        for i in range(N+1):
            dp[i][0][0]=0
            dp[i][0][1]=-2**31

        for i in range(N):
            for k in range(2,0,-1):
                dp[i+1][k][0]=max(dp[i][k][1]+prices[i],dp[i][k][0])
                dp[i+1][k][1]=max(dp[i][k-1][0]-prices[i],dp[i][k][1])
        return dp[-1][2][0]

'''
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。
注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
'''
class Solution4(object):
    def maxProfitInf(self, prices):
        """
        DP[n,{0,1}],第n天，可用操作数为k，状态：0：没有，1：持有
        DP表示当前手里的钱
        :type prices: List[int]
        :rtype: int
        """
        N=len(prices)
        if N==0:
            return 0
        dp=[[0,0] for _ in range(N)]
        dp[0][0]=0
        dp[0][1]=-prices[0]
        for i in range(1,N):
            dp[i][0]=max(dp[i-1][1]+prices[i],dp[i-1][0])
            dp[i][1]=max(dp[i-1][0]-prices[i],dp[i-1][1])
        return dp[-1][0]

    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        max_k=min(len(prices)//2,k)
        if k>max_k:
            return self.maxProfitInf(prices)  # 解决k太大，超内存情况，k太大就和k==inf一样。
        N=len(prices)
        if N==0:
            return 0
        dp=[[[0,0] for _ in range(max_k+1)] for _ in range(N+1)]
        # 还没有股票可买卖
        for k in range(max_k+1):
            dp[0][k][0]=0
            dp[0][k][1]=-2**31
        # 没有操作可执行
        for i in range(N+1):
            dp[i][0][0]=0
            dp[i][0][1]=-2**31

        for i in range(N):
            for k in range(max_k,0,-1):
                dp[i+1][k][0]=max(dp[i][k][1]+prices[i],dp[i][k][0])
                dp[i+1][k][1]=max(dp[i][k-1][0]-prices[i],dp[i][k][1])
        return dp[-1][max_k][0]

