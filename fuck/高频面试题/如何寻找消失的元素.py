

def missNumber(nums):
    n=len(nums)
    res=n-0
    for i,x in enumerate(nums):
        res+=i-x
    return res


print(missNumber([0,3,1,4,5]))