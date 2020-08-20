'''
给定一个包含非负整数的数组，你的任务是统计其中可以组成三角形三条边的三元组个数。

示例 1:
输入: [2,2,3,4]
输出: 3
解释:
有效的组合是:
2,3,4 (使用第一个 2)
2,3,4 (使用第二个 2)
2,2,3
注意:
数组长度不超过1000。
数组里整数的范围为 [0, 1000]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-triangle-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

def isvalid(a,b,c):
    return a+b>c

class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt=0
        N=len(nums)
        nums.sort()
        for i in range(N-2):
            for j in range(i+1,N-1):
                left=j+1
                right=N-1
                target=nums[i]+nums[j]
                while left<=right:
                    mid=(left+right)//2
                    if nums[mid]==target:
                        right=mid-1
                    elif nums[mid]<target:
                        left=mid+1
                    else:
                        right=mid-1
                k=j if right<j+1 or right>N-1 or nums[right]>=target else right
                cnt+=k-j
        return cnt

    def triangleNumber2(self, nums):
        N=len(nums)
        cnt=0
        nums.sort()
        for i in range(N-1,1,-1):
            left=0
            right=i-1
            while left<right:
                t=nums[left]+nums[right]
                if t>nums[i]:
                    cnt+=right-left
                    right-=1
                elif t<=nums[i]:
                    left+=1
        return cnt

if __name__ == '__main__':
    s=Solution()
    print(s.triangleNumber([1,2,3,4,5,6]))
    print(s.triangleNumber2([1, 2, 3, 4, 5, 6]))