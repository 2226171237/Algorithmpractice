
'''最短过河问题'''
def solve(nums):
    nums=sorted(nums)
    N=len(nums)
    sum=0
    i=N-1
    while i>2:
        if nums[0]+2*nums[1]+nums[i]>2*nums[0]+nums[i-1]+nums[i]:
            sum+=2*nums[0]+nums[i-1]+nums[i]
        else:
            sum+=nums[0]+2*nums[1]+nums[i]
        i-=2
    if i==2:
        sum+=nums[0]+nums[1]+nums[2]
    elif i==1:
        sum+=nums[1]
    else:
        sum+=nums[0]
    return sum

if __name__ == '__main__':
    print(solve([2,10,12,11]))
