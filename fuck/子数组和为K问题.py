
'''
给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。
示例 1 :
输入:nums = [1,1,1], k = 2
输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
说明 :
数组的长度为 [1, 20,000]。
数组中元素的范围是 [-1000, 1000] ，且整数 k 的范围是 [-1e7, 1e7]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subarray-sum-equals-k
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        cnt=0
        i=len(nums)-1
        while i>=0:
            if nums[i]==k:
                cnt+=1
            for j in range(i-1,-1,-1):
                nums[i]+=nums[j]
                if nums[i]==k:
                    cnt+=1
            i-=1
        return cnt

    def subarraySum2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        preSum=[0 for _ in range(len(nums)+1)] # 前n项的和,前缀和
        for i in range(len(nums)):
            preSum[i+1]=preSum[i]+nums[i]
        # sum(i,j)=preSum[j+1]-preSum[i]
        # for i in range(1,len(nums)+1):
        #     for j in range(i,len(nums)+1):  # 等价 if preSum[j+1]-k=preSum[i]:
        #         if preSum[j+1]-preSum[i]==k:
        #             cnt+=1
        # 两数之和
        hashset=dict()
        cnt=0
        for x in preSum:
            if x-k in hashset:
                cnt+=hashset[x-k]
            hashset[x] = hashset.get(x, 0) + 1
        return cnt

s=Solution()
print(s.subarraySum([1,1,1],2))
print(s.subarraySum2([1,1,1],2))