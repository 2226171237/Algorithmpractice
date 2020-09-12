# 给一个数组，如何同时求出最大值和最小值，如何同时求出最大值和第二大值？

# 返回最大最小值
def getMinAndMax(nums):
    min_i=0
    max_i=0
    for i in range(1,len(nums)):
        if nums[min_i]>nums[i]:
            min_i=i
        if nums[max_i]<nums[i]:
            max_i=i
    return nums[max_i],nums[min_i]

print(getMinAndMax([3,2,1,5,7,3]))

# 使用分治解决
def getMinAndMax2(nums,left,right):
    if left==right:
        return nums[left],nums[right]
    mid=(left+right)//2
    left_max,left_min=getMinAndMax2(nums,left,mid)
    right_max,right_min=getMinAndMax2(nums,mid+1,right)
    return max(left_max,right_max),min(left_min,right_min)

print(getMinAndMax2([3,2,1,5,7,3],0,5))

# 返回最大值，和第二值
def getMaxTopTwo(nums):
    assert len(nums)>=2
    max1_i=0 if nums[0]>nums[1] else 1
    max2_i=1-max1_i
    for i in range(2,len(nums)):
        if nums[i]>nums[max1_i]:
            max2_i=max1_i
            max1_i=i
        elif nums[i]>nums[max2_i]:
            max2_i=i
    return nums[max1_i],nums[max2_i]

print(getMaxTopTwo([3,2,1,5,7,3]))

# 通过分治解决
def getMaxTopTwo2(nums,left,right):
    if left==right:
        return nums[left],-2**31
    mid=(left+right)//2
    left_max1,left_max2=getMaxTopTwo2(nums,left,mid)
    right_max1,right_max2=getMaxTopTwo2(nums,mid+1,right)
    if left_max1>right_max1:
        merge_max1=left_max1
        merge_max2=max(left_max2,right_max1)
    else:
        merge_max1 = right_max1
        merge_max2 = max(right_max2,left_max1)
    return merge_max1,merge_max2
print(getMaxTopTwo2([3,2,1,5,7,3,6,9],0,7))


