

# 获取右边比当前元素更大的数，没有则是-1
# 单调递减栈
def getGreaterNumber(nums):
    stack=[]
    result=[-1 for _ in range(len(nums))]
    for i in range(len(nums)):
        while len(stack) and nums[stack[-1]]<nums[i]:
            result[stack[-1]]=nums[i]
            stack.pop()
        stack.append(i)
    return result

# 获取右边比当前元素更大的数，没有则是-1，数组是环形的
# 单调递减栈
def getGreaterNumber2(nums):
    stack=[]
    result=[-1 for _ in range(len(nums))]
    for k in range(len(nums)*2):
        i=k%len(nums)
        while len(stack) and nums[stack[-1]]<nums[i]:
            result[stack[-1]]=nums[i]
            stack.pop()
        stack.append(i)
    return result
print(getGreaterNumber([2,1,2,4,3]))
print(getGreaterNumber2([2,1,2,4,3]))