
class Solution:
    def binarySearch(self,nums,target):
        '''二查搜索，找到则返回索引，否则返回-1'''
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return -1

    def left_bound(self,nums,target):
        '''寻找左侧边界的二分搜索'''
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                right=mid-1
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        if left>=len(nums) or nums[left]!=target:
            return -1
        return left

    def right_bound(self,nums,target):
        '''寻找左侧边界的二分搜索'''
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                left=mid+1
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        if right<0 or nums[right]!=target:
            return -1
        return right

if __name__ == '__main__':
    s=Solution()
    print(s.left_bound([1,2,2,2,3,4,5],1))
    print(s.right_bound([1,2,2,2,3,4,5],1))
    print(chr(ord('A') | ord(' ')))
    print(chr(ord('a') & ord('_')))
    print(-2^-3)
    print(-2^3)
    print(2^3)