

def longestSubAseSeq(nums):
    '''
    dp[i] 表示以num[i] 结尾的最长上升子序长度
    dp[i]=max(dp[j]+1,dp[i]) 0<=j<i if nums[j]<num[i]
    :param nums:
    :return:
    '''
    N=len(nums)
    if N==0:
        return 0
    dp=[1 for _ in range(N)]
    maxLen=1
    for i in range(1,N):
        for j in range(i-1,-1,-1):
            if nums[j]<=nums[i]:
                dp[i]=max(dp[i],dp[j]+1)
        maxLen=max(maxLen,dp[i])
    return maxLen

print(longestSubAseSeq([2,3,1,4]))