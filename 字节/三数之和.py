'''
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？
请你找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

示例：
给定数组 nums = [-1, 0, 1, 2, -1, -4]，
满足要求的三元组集合为：
[ [-1, 0, 1],
  [-1, -1, 2]]
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def threeSum(self, nums):
        """
        递归，超时
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result=[]
        dup=set()
        def find(nums,i,path):
            if len(path)==3 and sum(path)==0:
                tmpPath=sorted(path)
                if tuple(tmpPath) not in dup:
                    result.append(tmpPath[:])
                    dup.add(tuple(tmpPath))
                return
            if i>=len(nums):
                return
            # 选择
            path.append(nums[i])
            find(nums,i+1,path)
            # 不选
            path.pop()
            find(nums,i+1,path)

        find(nums,0,[])
        return result

    def threeSum2(self, nums):
        '''排序+双指针'''
        nums=sorted(nums)
        result=[]
        i=0
        while i<len(nums):
            if nums[i]>0:
                break
            if 0<i and nums[i]==nums[i-1]:
                i+=1
                continue
            left=i+1
            right=len(nums)-1
            while left<right:
                x=nums[i]+nums[left]+nums[right]
                if x==0:
                    result.append([nums[i],nums[left],nums[right]])
                    left += 1
                    while left<right and nums[left]==nums[left-1]:
                        left+=1

                    right -= 1
                    while left<right and nums[right]==nums[right+1]:
                        right-=1
                elif x>0:
                    right-=1
                else:
                    left+=1
            i+=1
        return result
if __name__ == '__main__':
    s=Solution()
    # print(s.threeSum([6,-5,-6,-1,-2,8,-1,4,-10,-8,-10,-2,-4,-1,-8,-2,8,9,-5,-2,-8,-9,-3,-5]))
    print(s.threeSum2([6, -5, -6, -1, -2, 8, -1, 4, -10, -8, -10, -2, -4, -1, -8, -2, 8, 9, -5, -2, -8, -9, -3, -5]))