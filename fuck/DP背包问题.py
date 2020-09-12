
# 0-1 背包问题
# 给你一个可装载重量为W的背包和N个物品，每个物品有重量和价值两个属性。
# 其中第i个物品的重量为wt[i]，价值为val[i]，现在让你用这个背包装物品，
# 最多能装的价值是多少？

def maxValue(wt,val,W):
    N=len(wt)
    dp=[[0 for _ in range(W)] for _ in range(N)]
    for w in range(1,W+1):
        i=w-1
        if wt[0]<=w:
            dp[0][i]=val[0]
    for i in range(1,N):
        for w in range(1,W+1):
            dp[i][w-1]=dp[i-1][w-wt[i]-1]+val[i] if w-wt[i]-1>=0 else 0  # 选择装 i
            dp[i][w-1]=max(dp[i][w-1],dp[i-1][w-1])                      # 选择不装 i
    return dp[-1][-1]
print(maxValue([2,1,3],[4,2,3],4))

# 0-1 背包问题的变体
# 二维DP变成一维DP，就是状态压缩
# 问题：分割等和子集 一个正整数数组，是否可以将数组分成两个子集，使两个子集的和相等？

def canSplitArray1(nums):
    total_sum=sum(nums)
    if total_sum & 1==1:
        return False
    target=total_sum//2
    max_target=maxValue(nums,nums,target)  # 转化成背包问题
    return max_target==target

print(canSplitArray1([1,5,5,11]))

def canSplitArray2(nums):
    total_sum=sum(nums)
    if total_sum & 1==1:
        return False
    target=total_sum//2
    # 定义dp[i][j] 为装前i个物体，背包为j 是否可以刚好装满
    dp=[[False for _ in range(target+1)] for _ in range(len(nums)+1)]
    dp[0][0]=True
    for i in range(1,target+1):
        dp[0][i]=False
    for i in range(1,len(nums)+1):
        dp[i][0]=True
    for i in range(1,len(nums)+1):
        for j in range(1,target+1):
            dp[i][j]=dp[i-1][j-nums[i-1]] if j-nums[i-1]>=0 else False
            dp[i][j]=dp[i][j] or dp[i-1][j]
    return dp[-1][-1]

print(canSplitArray2([1,5,11,5]))

# 注意到dp[i][j]都是通过上一行dp[i-1][..]转移过来的，之前的数据都不会再使用了。
# 所以，我们可以进行状态压缩，将二维dp数组压缩为一维，节约空间复杂度：

def canSplitArray3(nums):
    total_sum=sum(nums)
    if total_sum & 1==1:
        return False
    target=total_sum//2
    # 定义dp[i][j] 为装前i个物体，背包为j 是否可以刚好装满
    dp=[False for _ in range(target+1)]
    dp[0]=True
    for i in range(len(nums)):
        for j in range(target,0,-1):  # 要从右往左，防止使用刷新后的数组
            dp[j]=dp[j] or dp[j-nums[i]] if j-nums[i]>=0 else False
    return dp[-1]

print(canSplitArray3([1,5,11,5]))

# leetcode 518 零钱兑换2

def coinCout(coins,amount):
    cnt=[0]
    def dfs(i,cur_amount):
        if cur_amount==amount:
            cnt[0]+=1
            return
        if cur_amount>amount:
            return
        if i>=len(coins):
            return
        for j,x in enumerate(coins[i:]):
            dfs(j+i,cur_amount+x)
    dfs(0,0)
    return cnt[0]
print(coinCout([1,2,5],5))

def coinCount2(coins,amount):
    N=len(coins)
    coins=sorted(coins)
    dp=[[0 for _ in range(amount+1)] for _ in range(N+1)]
    for i in range(N+1):
        dp[i][0]=1
    for i in range(1,N+1):
        for j in range(1,amount+1):
            # 一个物体可重复多次，所以是dp[i][j-coins[i-1]] 而不是dp[i-1][j-coins[i-1]](一个物体就使用一次)
            dp[i][j]=dp[i][j-coins[i-1]] if j-coins[i-1]>=0 else 0
            dp[i][j]+=dp[i-1][j]
    return dp[-1][-1]

print(coinCount2([1,2,5],5))


def coinCount2(coins,amount):
    N=len(coins)
    coins=sorted(coins)
    dp=[0 for _ in range(amount+1)]
    dp[0]=1
    for i in range(1,N+1):
        for j in range(1,amount+1):
            dp[j]+=dp[j-coins[i-1]] if j-coins[i-1]>=0 else 0
    return dp[-1]

print(coinCount2([1,2,5],5))
