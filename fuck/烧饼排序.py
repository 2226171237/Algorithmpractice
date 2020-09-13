


def getMaxId(nums,n):
    max_i=0
    for i in range(1,n+1):
        if nums[max_i]<nums[i]:
            max_i=i
    return max_i

def reverse(nums,low,high):
    while low<high:
        nums[low],nums[high]=nums[high],nums[low]
        low+=1
        high-=1

def sort(nums,n):
    '''对前n个元素进行排序，设法将最大值翻转到最后一个位置，然后递归'''
    if n==0:
        return
    max_i=getMaxId(nums,n)
    if max_i<n:
        reverse(nums,0,max_i)
        reverse(nums,0,n)
    sort(nums,n-1)


import random
nums=[random.randint(0,20) for _ in range(20)]
print(nums)
sort(nums,len(nums)-1)
print(nums)


