'''
给你一个整数数组 nums，请你将该数组升序排列。

示例 1：
输入：nums = [5,2,3,1]
输出：[1,2,3,5]
示例 2：
输入：nums = [5,1,1,2,0,0]
输出：[0,0,1,1,2,5]
 
提示：
1 <= nums.length <= 50000
-50000 <= nums[i] <= 50000
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sort-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


def partition(nums,low,high):
    base=nums[low]
    while low<high:
        while low<high and nums[high]>base:
            high-=1
        nums[low]=nums[high]
        while low<high and nums[low]<=base:
            low+=1
        nums[high]=nums[low]
    nums[low]=base
    return low

def qsort(nums,low,high):
    if low>=high:
        return
    mid=partition(nums,low,high)
    qsort(nums,low,mid-1)
    qsort(nums,mid+1,high)

class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        qsort(nums,0,len(nums)-1)
        return nums



if __name__ == '__main__':
    s=Solution()
    print(s.sortArray([5,2,3,1]))
