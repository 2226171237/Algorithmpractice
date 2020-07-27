
'''
问题1：背包问题
有N个物品，每个物体重 w_i,价值v_i。你有一个最大容量为K的背包，求背包可装入的物品的最大总价值。
dp[n,k] 定义为前n个物品，背包大小为k时可以装下的最大价值。
'''
def getMaxValueBag(weights,values,K):
    N=len(weights)
    dp=[[0 for _ in range(K+1)] for _ in range(N)]
    for k in range(1,K+1):
        if weights[0]>k:
            dp[0][k]=0
        else:
            dp[0][k]=values[0]
    for n in range(1,N):
        for k in range(1,K+1):
            if weights[n]>k: # 装不下物品n
                dp[n][k]=dp[n-1][k]
            else:
                dp[n][k]=max(values[n]+dp[n-1][k-weights[n]],dp[n-1][k]) # 装物品n,不装物品n
    return dp[-1][-1]


print(getMaxValueBag([4,3,1,1],[3000,2000,1500,2000],4))


# 石头游戏
def stoneGame(stones):
    N=len(stones)
    first=[[0 for _ in range(N)] for _ in range(N)] # 先手
    second=[[0 for _ in range(N)] for _ in range(N)] # 后手
    # 基本情况
    for i in range(N):
        first[i][i]=stones[i]
        second[i][i]=0

    for jj in range(1,N):
        for i in range(0,N-jj):
            j=i+jj
            left=stones[i]+second[i+1][j]
            right=stones[j]+second[i][j-1]
            if left>right:
                first[i][j]=left
                second[i][j]=first[i+1][j]
            else:
                first[i][j]=right
                second[i][j]=first[i][j-1]
    return first[0][-1]-second[0][-1]

print(stoneGame([3,9,1,2]))

