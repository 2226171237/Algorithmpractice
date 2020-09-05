
# 问题1：最多完成k次交易的最大收益
def maxProofK(prices,k):
    N=len(prices)
    if N==0:
        return 0
    # dp[i][s][k]  第i天的钱数，s=0: 手里没有股票，s=1: 手里有股票，k: 剩余的操作数
    dp=[[[0 for _ in range(k+1)] for _ in range(2)] for _ in range(N)]
    for i in range(N):
        dp[i][0][0]=0
        dp[i][1][0]=-2**31
    for t in range(1,k+1):
        dp[0][0][t]=0
        dp[0][1][t]=-prices[0]
    maxMoney=0
    for i in range(1,N):
        for t in range(1,k+1):
            dp[i][0][t]=max(dp[i-1][0][t],dp[i-1][1][t]+prices[i])
            dp[i][1][t]=max(dp[i-1][0][t-1]-prices[i],dp[i-1][1][t])  # 只有买才把操作减1，买和不操作，操作数不变
            maxMoney=max(maxMoney,dp[i][0][t],dp[i][1][t])
    return maxMoney

print(maxProofK([3,2,6,5,0,3],1))

# 问题2： k=+inf 次交易最大盈利
def maxProof(prices):
    N=len(prices)
    if N==0:
        return 0
    # dp[i][s]  第i天的钱数，s=0: 手里没有股票，s=1: 手里有股票
    dp=[[0 for _ in range(2)] for _ in range(N)]
    dp[0][0]=0
    dp[0][1]=-prices[0]
    maxMony=0
    for i in range(1,N):
        dp[i][0]=max(dp[i-1][0],dp[i-1][1]+prices[i])
        dp[i][1]=max(dp[i-1][1],dp[i-1][0]-prices[i])
        maxMony=max(dp[i][0],dp[i][1],maxMony)
    return maxMony

print(maxProof([3,2,6,5,0,3]))

# 问题3： k=1 次交易最大盈利
def maxProof1(prices):
    N=len(prices)
    if N==0:
        return 0
    # dp[i][s]  第i天的钱数，s=0: 手里没有股票，s=1: 手里有股票
    dp=[[0 for _ in range(2)] for _ in range(N)]
    dp[0][0]=0
    dp[0][1]=-prices[0]
    maxMony=0
    for i in range(1,N):
        dp[i][0]=max(dp[i-1][0],dp[i-1][1]+prices[i])
        dp[i][1]=max(dp[i-1][1],-prices[i])
        maxMony=max(dp[i][0],dp[i][1],maxMony)
    return maxMony

print(maxProof1([3,2,6,5,0,3]))

# 问题4：k=+inf 次交易最大盈利，且每次 sell 之后要等一天才能继续交易
def maxProofInf(prices):
    N=len(prices)
    if N==0:
        return 0
    # dp[i][s]  第i天的钱数，s=0: 手里没有股票，s=1: 手里有股票
    dp=[[0 for _ in range(2)] for _ in range(N)]
    dp[0][0]=0
    dp[0][1]=-prices[0]
    maxMony=0
    for i in range(1,N):
        dp[i][0]=max(dp[i-1][0],dp[i-1][1]+prices[i])  # sell
        dp[i][1]=max(dp[i-1][1],dp[i-2][0]-prices[i] if i-2>=0 else -prices[i])  # buy
        maxMony=max(dp[i][0],dp[i][1],maxMony)
    return maxMony

print(maxProofInf([3,2,6,5,0,3]))


# 问题5：k=+inf，每次交易要支付手续费，只要把手续费从利润中减去即可
def maxProof3(prices,free):
    N=len(prices)
    if N==0:
        return 0
    # dp[i][s]  第i天的钱数，s=0: 手里没有股票，s=1: 手里有股票
    dp=[[0 for _ in range(2)] for _ in range(N)]
    dp[0][0]=0
    dp[0][1]=-prices[0]-free
    maxMony=0
    for i in range(1,N):
        dp[i][0]=max(dp[i-1][0],dp[i-1][1]+prices[i])  # sell
        dp[i][1]=max(dp[i-1][1],dp[i-1][0]-prices[i]-free)  # buy
        maxMony=max(dp[i][0],dp[i][1],maxMony)
    return maxMony

print(maxProof3([3,2,6,5,0,3],1))


# 问题5：k=anyvalue的改进
def maxProofK(prices,k):
    N=len(prices)
    if N==0:
        return 0
    if k>=N//2:
        return maxProofInf(prices)
    # dp[i][s][k]  第i天的钱数，s=0: 手里没有股票，s=1: 手里有股票，k: 剩余的操作数
    dp=[[[0 for _ in range(k+1)] for _ in range(2)] for _ in range(N)]
    for i in range(N):
        dp[i][0][0]=0
        dp[i][1][0]=-2**31
    for t in range(1,k+1):
        dp[0][0][t]=0
        dp[0][1][t]=-prices[0]
    maxMoney=0
    for i in range(1,N):
        for t in range(1,k+1):
            dp[i][0][t]=max(dp[i-1][0][t],dp[i-1][1][t]+prices[i])
            dp[i][1][t]=max(dp[i-1][0][t-1]-prices[i],dp[i-1][1][t])  # 只有买才把操作减1，买和不操作，操作数不变
            maxMoney=max(maxMoney,dp[i][0][t],dp[i][1][t])
    return maxMoney


