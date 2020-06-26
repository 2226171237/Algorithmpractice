'''
输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。
如果有多对数字的和等于s，则输出任意一对即可。

示例 1：
输入：nums = [2,7,11,15], target = 9
输出：[2,7] 或者 [7,2]

限制：
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^6
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/he-wei-sde-liang-ge-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        low=0
        high=len(nums)-1
        result=[]
        while low<high:
            if nums[low]+nums[high]>target:
                high-=1
            elif nums[low]+nums[high]<target:
                low+=1
            else:
                result.extend([nums[low],nums[high]])
                break
        return result

if __name__ == '__main__':
    s=Solution()
    print(s.twoSum([2,7,11,23],9))

