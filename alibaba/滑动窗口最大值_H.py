'''
给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。
你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

返回滑动窗口中的最大值。
进阶：
你能在线性时间复杂度内解决此题吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sliding-window-maximum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        Q=deque()
        for i in range(k):
            while len(Q)>0 and nums[Q[-1]]<nums[i]:
                Q.pop()
            Q.append(i)
        result=[nums[Q[0]]]
        for i in range(k,len(nums)):
            while len(Q) and nums[i]>nums[Q[-1]]:
                Q.pop()
            Q.append(i)
            while len(Q) and i-Q[0]>=k:
                Q.popleft()
            result.append(nums[Q[0]])
        return result

if __name__ == '__main__':
    s=Solution()
    print(s.maxSlidingWindow([8,3,-1,-3,5,3,6,7],2))

