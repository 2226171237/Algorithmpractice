'''
统计一个数字在排序数组中出现的次数。

示例 1:
输入: nums = [5,7,7,8,8,10], target = 8
输出: 2
示例 2:
输入: nums = [5,7,7,8,8,10], target = 6
输出: 0

限制：
0 <= 数组长度 <= 50000
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        begin=0
        end=len(nums)-1
        while begin<=end:
            mid=(begin+end)//2
            if nums[mid]>target:
                end=mid-1
            elif nums[mid]<target:
                begin=mid+1
            else:
                left=mid
                while left>=0 and nums[left]==target:
                    left-=1
                right=mid
                while right<len(nums) and nums[right]==target:
                    right+=1
                return right-left-1
        return 0

if __name__ == '__main__':
    s=Solution()
    print(s.search([5,7,7,8,8,10],8))