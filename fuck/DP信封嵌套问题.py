
# leetcode 354
# 大信封装小信封。
# 先按 w进行升序，h进行降序排序，然后对h数组寻找最长上升子序。

def longOfSubSeq(nums):
    n=len(nums)
    if 0==n:
        return 0
    dp=[1 for _ in range(n)]
    maxLen=1
    for i in range(1,n):
        for j in range(i-1,-1,-1):
            if nums[i]>nums[j]:
                dp[i]=max(dp[j]+1,dp[i])
        maxLen=max(maxLen,dp[i])
    return maxLen

def compare(a,b):
    if a[0]>b[0]:
        return 1
    elif a[0]==b[0]:
        if a[1]<b[1]:
            return 1
        else:
            return -1
    else:
        return -1
from functools import cmp_to_key

def getLetterNums(letters):
    letters=sorted(letters,key=cmp_to_key(compare))
    nums=[x[1] for x in letters]
    return longOfSubSeq(nums)

print(getLetterNums([[5,4],[6,4],[6,7],[2,3]]))