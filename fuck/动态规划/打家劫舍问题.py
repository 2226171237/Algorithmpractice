
# 选与不选
def rub(nums):
    # 返回nums[start:]可抢的最多钱,动态规划递归
    def dp(nums,start):
        if start>=len(nums):
            return 0
        res=max(dp(nums,start+1),dp(nums,start+2)+nums[start]) # 不抢与抢 ,抢则跳过下一个
        return res
    return dp(nums,0)


def rub2(nums):
    '''动态规划加记忆化，解决重复子问题,也就是自顶向下'''
    mem=dict()
    def dp(nums,start):
        if start in mem:
            return mem[start]
        if start>=len(nums):
            return 0
        res=max(dp(nums,start+1),dp(nums,start+2)+nums[start]) # 不抢与抢 ,抢则跳过下一个
        mem[start]=res
        return res
    return dp(nums,0)

def rub3(nums):
    '''自顶向上'''
    dp=[0 for _ in range(len(nums)+2)]
    for i in range(len(nums)-1,-1,-1):
        dp[i]=max(dp[i+1],dp[i+2]+nums[i])
    return dp[0]

def rub4(nums):
    '''自顶向上,优化空间复杂度'''
    dp=[0,0,0]
    for i in range(len(nums)-1,-1,-1):
        dp[0]=max(dp[1],dp[2]+nums[i])
        dp[2]=dp[1]
        dp[1]=dp[0]
    return dp[0]

def rubRange(nums):
    if len(nums)==1:
        return nums[0]
    def dp(nums):
        dp = [0, 0, 0]
        for i in range(len(nums) - 1, -1, -1):
            dp[0] = max(dp[1], dp[2] + nums[i])
            dp[2] = dp[1]
            dp[1] = dp[0]
        return dp[0]
    return max(dp(nums[:-1]),dp(nums[1:]))

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def rubTree(root):
    mem=dict()
    def dp(root):
        if root in mem:
            return mem[root]
        if None==root:
            return 0
        un_rub=dp(root.left)+dp(root.right) # 不抢root
        do_rub=root.val+(0 if root.left==None else dp(root.left.left)+dp(root.left.right))+\
               (0 if root.right==None else dp(root.right.left)+dp(root.right.right))
        res=max(un_rub,do_rub)
        mem[root]=res
        return res
    return dp(root)


root=TreeNode(3)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.right=TreeNode(3)
root.right.right=TreeNode(1)
print(rubTree(root))

