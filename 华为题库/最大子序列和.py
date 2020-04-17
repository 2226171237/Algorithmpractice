'''
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:
输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

进阶:
如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def maxSubArray(self, nums) -> int:
        '''
        动态规划，P(i) 表示为以i为结束元素的最大子序列和，P(i)=max(sum[x(j),x(j+1),..,x(i)]) 0<=j<=i，必须以包含x(i)结束的子序
        :param list[int] nums:
        :return: int
        '''
        if len(nums)==0:
            return 0
        P=[0 for _ in range(len(nums))]
        maxSum=nums[0]
        P[0]=maxSum
        i=1
        while i<len(nums):
            if P[i-1]>=0:
                P[i]=P[i-1]+nums[i]
            else:
                P[i]=nums[i]
            maxSum=max(maxSum,P[i])
            i+=1
        return maxSum

if __name__ == '__main__':
    S=Solution()
    print(S.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
