'''
给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。
'''

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        N=len(nums)
        if N==0:
            return []
        result=[]

        return result

if __name__ == '__main__':
    s=Solution()
    print(s.maxSlidingWindow([1,3,-1,-3,5,3,6,7],2))