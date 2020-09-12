

def getNextGreater(nums):
    stack=[]  # 单减堆栈
    result=[-1 for _ in range(len(nums))]
    for i,x in enumerate(nums):
        if len(stack)==0:
            stack.append(i)
        else:
            while len(stack) and nums[stack[-1]]<nums[i]:
                result[stack[-1]]=nums[i]
                stack.pop()
            stack.append(i)
    return result

print(getNextGreater([3,2,1,4,5,7,0,8,1,2]))


def getNextGreater2(nums):
    stack=[]  # 单减堆栈
    result=[-1 for _ in range(len(nums))]
    for i in range(len(nums)-1,-1,-1):
        if len(stack)==0:
            stack.append(nums[i])
            result[i]=-1
        else:
            while len(stack) and stack[-1]<=nums[i]:
                stack.pop()
            result[i]=stack[-1] if len(stack) else -1
            stack.append(nums[i])
    return result
print(getNextGreater2([3,2,1,4,5,7,0,8,1,2]))


# 环状数据
def getNextGreater3(nums):
    stack=[]  # 单减堆栈
    result=[-1 for _ in range(len(nums))]
    for j in range(2*len(nums)-1,-1,-1):
        i=j%len(nums)
        if len(stack)==0:
            stack.append(nums[i])
            result[i]=-1
        else:
            while len(stack) and stack[-1]<=nums[i]:
                stack.pop()
            result[i]=stack[-1] if len(stack) else -1
            stack.append(nums[i])
    return result

print(getNextGreater3([3,2,1,4,5,7,0,8,1,2]))

