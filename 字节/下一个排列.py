'''
实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
必须原地修改，只允许使用额外常数空间。

以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/next-permutation
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

def getOne(arr):
    i=len(arr)-1
    j=len(arr)-2
    while j>=0:
        if arr[j]<arr[i]:
            return j
        i-=1
        j-=1
    else:
        return -1

def getTwo(arr,i):
    M=arr[i+1]
    k=i+1
    for j in range(i+1,len(arr)):
        if arr[j]>arr[i] and arr[j]<=M:
            M=arr[j]
            k=j
    return k

def reverse(arr,low,high):
    while low < high:
        arr[low], arr[high] = arr[high], arr[low]
        low += 1
        high -= 1

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i=getOne(nums)
        if i<0:
            reverse(nums,0,len(nums)-1)
            return
        j=getTwo(nums,i)
        nums[i],nums[j]=nums[j],nums[i]
        low=i+1
        high=len(nums)-1
        reverse(nums,low,high)

if __name__ == '__main__':
    s=Solution()
    nums=[1]
    print(s.nextPermutation(nums))
    print(nums)