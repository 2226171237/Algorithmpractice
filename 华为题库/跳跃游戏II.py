'''
给定一个非负整数数组，你最初位于数组的第一个位置。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
你的目标是使用最少的跳跃次数到达数组的最后一个位置。

示例:
输入: [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
说明:假设你总是可以到达数组的最后一个位置。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/jump-game-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def jump1(self, nums:list) -> int:
        '''
        贪心算法
        :param list[int] nums:
        :return: int
        '''
        steps=0
        end=0  # 终点位置
        maxpostion=0
        for i in range(len(nums)-1):
            maxpostion=max(maxpostion,nums[i]+i)  # 可以跳到的最远的位置
            if i==end: # 到达该次终点，更新终点
                end=maxpostion
                steps+=1
        return steps
    def jump2(self, nums:list) -> int:
        '''
        贪心算法
        :param list[int] nums:
        :return: int
        '''
        start=0
        steps=0
        while start<len(nums)-1:
            maxPosition=nums[start]+start # 在start处可以跳的最远位置
            if maxPosition>=len(nums)-1:
                return steps+1
            start += 1
            maxthisPosition=nums[start]+start  # 选择可以跳到最远位置的点,贪心
            for i in range(start,maxPosition+1):
                if nums[i]+i>=maxthisPosition:
                    maxthisPosition=nums[i]+i
                    start=i
            steps+=1

        return steps


if __name__ == '__main__':
    S=Solution()
    print(S.jump1([10,9,8,7,6,5,4,3,2,1,1,0]))
    print(S.jump2([10,9,8,7,6,5,4,3,2,1,1,0]))


