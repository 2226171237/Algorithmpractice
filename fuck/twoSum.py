
# 给你一个数组和一个整数target，可以保证数组中存在两个数的和为target，请你返回这两个数的索引。

def twoSum1(nums,target):
    hash_map=dict()
    for i,x in enumerate(nums):
        if target-x in hash_map:
            return i,hash_map[target-x]
        hash_map[x]=i
    return -1,-1

print(twoSum1([1,2,3,4,5],8))

# 输入序列有序，怎么优化：双指针
def twoSum2(nums,target):
    left=0
    right=len(nums)-1
    while left<right:
        t=nums[left]+nums[right]
        if t<target:
            left+=1
        elif t>target:
            right-=1
        else:
            return left,right
    return -1,-1

print(twoSum1([1,2,3,4,5],8))