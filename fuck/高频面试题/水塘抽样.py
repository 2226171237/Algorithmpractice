
import random
# 不知数组大小，随机选择一个元素
def getRandom(nums):
    res=nums[0]
    for i in range(1,len(nums)):
        rand_i=random.randint(0,i)
        if rand_i==0:  # 1/i的概率选择nums[i]
            res=nums[i]
    return res


def getRandomK(nums,k):
    res=[]
    for i in range(k):
        res.append(nums[i])
    for i in range(k+1,len(nums)):
        rand_i=random.randint(0,i)
        if rand_i<k:  # k/i的概率选择nums[i]
            res[rand_i]=nums[i]
    return res


print(getRandom([1,2,3,4,5,6,7]))
print(getRandomK([1,2,3,4,5,6,7],3))