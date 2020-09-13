
# 跳跃游戏1
# 给定一个非负整数数组，你最初位于数组的第一个位置。
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
# 判断你是否能够到达最后一个位置。
#
# 示例 1:
# 输入: [2,3,1,1,4]
# 输出: true
# 解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。

class Solution1(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        maxPosition = 0
        for i, x in enumerate(nums):
            if x == 0 and maxPosition <= i and i != n - 1:
                return False
            curPosition = i + x
            maxPosition = max(maxPosition, curPosition)
        return maxPosition >= len(nums) - 1

# 问题2：给定一个非负整数数组，你最初位于数组的第一个位置。
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
# 你的目标是使用最少的跳跃次数到达数组的最后一个位置。
#
# 示例:
# 输入: [2,3,1,1,4]
# 输出: 2
# 解释: 跳到最后一个位置的最小跳跃数是 2。
#      从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
# 假设你总是可以到达数组的最后一个位置。
class Solution2(object):
    def jump(self, nums):
        """
        贪心算法
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        end=0
        maxPos=0
        jumps=0
        for i in range(n-1):
            maxPos=max(maxPos,i+nums[i])
            if end==i:
                jumps+=1
                end=maxPos
        return jumps

    def jump2(self, nums):
        n=len(nums)
        cnt=0
        i=0
        while i<n-1:
            if i+nums[i]>=n-1:
                return cnt+1
            max_j=i
            for j in range(i+1,min(i+nums[i]+1,n)):
                if nums[j]+j>=nums[max_j]+max_j:
                    max_j=j
            if max_j==i:
                i=max_j+nums[max_j]
            else:
                i=max_j
            cnt+=1
        return cnt

s=Solution2()
print(s.jump([3,2,1]))
print(s.jump2([3,2,1]))





