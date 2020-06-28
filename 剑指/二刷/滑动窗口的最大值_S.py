'''
给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。
'''

from collections import deque
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
        Q=deque()
        Q.append(0)

        if k==1:
            result.append(nums[0])
        for i in range(1,N):
            while len(Q) and nums[Q[-1]]<nums[i]:
                Q.pop()
            Q.append(i)
            if i>=k-1:
                while len(Q) and i-Q[0]>=k:
                    Q.popleft()
                result.append(nums[Q[0]])
        return result

if __name__ == '__main__':
    s=Solution()
    print(s.maxSlidingWindow([1,3,1,2,0,5],3))