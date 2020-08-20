'''
一个正元素数组nums，给其添加正负号使其和为S，返回一共有多少种添符号的方法个数
'''
def func(nums,S):
    N=len(nums)
    cnt=0
    total=sum(nums)
    nums.sort()
    for i in range(0,N):
        this_sum=0
        for j in range(i,N):
            this_sum+=nums[j]
            T = 2 * this_sum - total
            if T == S:
                cnt += 1
            elif T > S:
                break
    if -total==S:
        cnt+=1
    return cnt


if __name__ == '__main__':
    print(func([4,3,1,2],0))
