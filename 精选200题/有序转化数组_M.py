'''
leetcode:360
给你一个已经 排好序 的整数数组 nums 和整数 a、b、c。对于数组中的每一个数 x，
计算函数值 f(x) = ax2 + bx + c，请将函数值产生的数组返回。
要注意，返回的这个数组必须按照 升序排列，并且我们所期望的解法时间复杂度为 O(n)。

示例 1：
输入: nums = [-4,-2,2,4], a = 1, b = 3, c = 5
输出: [3,9,15,33]

示例 2：
输入: nums = [-4,-2,2,4], a = -1, b = 3, c = 5
输出: [-23,-5,1,7]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sort-transformed-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def sortTransformedArray(self, nums, a: int, b: int, c: int):
        '''

        :param list[int] nums:
        :param a:
        :param b:
        :param c:
        :return:
        '''
        def f(x):
            return a*x*x+b*x+c
        if a==0:
            return [f(x) for x in nums]
        elif a<0:
            left,right=0,len(nums)-1
            result=[]
            while left<=right:
                x1= f(nums[left])
                x2=f(nums[right])
                if x1>x2:
                    result.append(x2)
                    right-=1
                else:
                    result.append(x1)
                    left+=1
            return result
        else:
            result=[]
            mid_x=-b/(2*a)
            mid_i=0
            for i in range(len(nums)):
                if mid_x-nums[i]>=0:
                    mid_i=i
            left,right=mid_i,mid_i+1
            while 0>=left and right<len(nums):
                x1 = f(nums[left])
                x2 = f(nums[right])
                if x1>x2:
                    result.append(x2)
                    right+=1
                else:
                    result.append(x1)
                    left-=1

            while left>=0:
                result.append(f(nums[left]))
                left-=1
            while right<len(nums):
                result.append(f(nums[right]))
                right += 1
            return result
if __name__ == '__main__':
    S=Solution()
    print(S.sortTransformedArray([-4,-2,2,4],1,3,5))
