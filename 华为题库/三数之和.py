'''
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。
注意：答案中不可以包含重复的三元组。
示例：
给定数组 nums = [-1, 0, 1, 2, -1, -4]，
满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def threeSum(self, nums):
        '''
        先排序，然后双指针
        :param list[int] nums:
        :return: list[list[int]]
        '''
        if len(nums)<=2:
            return []
        result=[]
        nums=sorted(nums)
        for i in range(len(nums)):
            if nums[i]>0:
                return result
            if i>0 and nums[i]==nums[i-1]:
                continue
            left=i+1
            right=len(nums)-1
            while right>left:
                sum=nums[i]+nums[left]+nums[right]
                if sum>0:
                    right-=1
                elif sum<0:
                    left+=1
                else:
                    result.append([nums[i],nums[left],nums[right]])
                    while right > left and nums[left] == nums[left + 1]:
                        left += 1
                    while right>left and nums[right]==nums[right-1]:
                        right-=1
                    left+=1
                    right-=1
        return result

if __name__ == '__main__':
    S=Solution()
    print(S.threeSum([0,0,0]))