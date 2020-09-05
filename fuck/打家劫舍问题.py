

def robber(prices):
    N=len(prices)
    if 0==N:
        return 0
    # dp[i][s]: 第i个房间的最大收益，s=0:不偷，s=1:偷
    dp=[[0,0] for _ in range(N+1)]
    dp[1][0]=0
    dp[1][1]=prices[0]
    maxSumP=prices[0]
    for i in range(1,N+1):
        dp[i][0]=dp[i-1][1]
        dp[i][1]=dp[i-1][0]+prices[i-1]
        maxSumP=max(maxSumP,dp[i][1],dp[i][0])
    return maxSumP

print(robber([2,7,9,3,1]))


def robber2(prices):
    '''dp[i] 以i为开始，到最后可以强到的最多的钱'''

    def dp(i):
        if i>=len(prices):
            return 0
        res=max(prices[i]+dp(i+2),dp(i+1))
        return res
    return dp(0)

print(robber2([2,7,9,3,1]))

def robber3(prices):
    '''dp[i] 以i为开始，到最后可以强到的最多的钱'''
    mem=dict()
    def dp(i):
        if i in mem:
            return mem[i]
        if i>=len(prices):
            return 0
        res=max(prices[i]+dp(i+2),dp(i+1))
        mem[i]=res
        return res
    return dp(0)

print(robber3([2,7,9,3,1]))

def robber4(prices):
    '''自底向上动态规划'''
    N=len(prices)
    dp=[0 for _ in range(N+2)]
    for i in range(N-1,-1,-1):
        dp[i]=max(prices[i]+dp[i+2],dp[i+1])
    return dp[0]

print(robber4([2,7,9,3,1]))

# **这些房子不是一排，而是围成了一个圈**。
# 首先，首尾房间不能同时被抢，那么只可能有三种不同情况：要么都不被抢；要么第一间房子被抢最后一间不抢；要么最后一间房子被抢第一间不抢。
# 那就简单了啊，这三种情况，那种的结果最大，就是最终答案呗！不过，其实我们不需要比较三种情况，只要比较情况二和情况三就行了，
# 因为这两种情况对于房子的选择余地比情况一大呀，房子里的钱数都是非负数，所以选择余地大，最优决策结果肯定不会小。
def robber5(prices):
    if len(prices)==1:
        return prices[0]
    return max(robber4(prices[:-1]),robber4(prices[1:]))
print(robber5([2,7,9,3,1]))

# 第三题又想法设法地变花样了，此强盗发现现在面对的房子不是一排，不是一圈，而是一棵二叉树！房子在二叉树的节点上，
# 相连的两个房子不能同时被抢劫，果然是传说中的高智商犯罪：
class TreeNode:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

def robber6(root):
    mem=dict()
    def dfs(root):
        if root in mem:
            return mem[root]
        if None==root:
            return 0
        res1=dfs(root.left)+dfs(root.right)  # 不抢root
        res2=root.val  # 抢root
        if root.left:
            res2+=dfs(root.left.left)+dfs(root.left.right)
        if root.right:
            res2+=dfs(root.right.left)+dfs(root.right.right)
        res=max(res1,res2)
        mem[root]=res
        return res
    return dfs(root)

root=TreeNode(3)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.right=TreeNode(3)
root.right.right=TreeNode(1)
print(robber6(root))
