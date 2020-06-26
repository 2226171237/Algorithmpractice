'''
输入一个整型数组，数组里有正数也有负数。数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。
要求时间复杂度为O(n)。
'''

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSum=float('-inf')
        P=-1
        for x in nums:
            if P>0:
                P+=x
            else:
                P=x
            maxSum = max(P, maxSum)
        return maxSum

if __name__ == '__main__':
    s=Solution()
    print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
