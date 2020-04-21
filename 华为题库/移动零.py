'''
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:
输入: [0,1,0,3,12]
输出: [1,3,12,0,0]

说明:
必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/move-zeroes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        遇到0则跟新零队列开始于结束位置，否则，交换
        :param list[int] nums
        """
        if len(nums) <= 1:
            return
        begin = -1
        end = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                if begin == -1:
                    begin = i
                end = i
            else:
                if begin != -1:
                    t = nums[i]
                    for j in range(begin, end + 1):
                        nums[j + 1] = 0
                    nums[begin] = t
                    begin += 1
                    end += 1
    def moveZeroes2(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        优化，不需每个零都移动
        :param list[int] nums
        """
        if len(nums)<=1:
            return
        m=0
        for i in range(len(nums)):
            if nums[i]==0:
                m+=1
            else:
                if m:
                    nums[i-m]=nums[i]
                    nums[i] = 0

if __name__ == '__main__':
    S=Solution()
    nums=[1,0,0,3,12]
    S.moveZeroes(nums)
    print(nums)