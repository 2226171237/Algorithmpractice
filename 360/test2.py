


from collections import  deque

import sys

def opt2(nums,begin):
    pt=begin
    for _ in range(len(nums)//2):
        pt_2=(pt+1)%len(nums)
        nums[pt],nums[pt_2]=nums[pt_2],nums[pt]
        pt=(pt+2)%len(nums)

def solve(N,opts):
    nums=[i+1 for i in range(N)]
    i=0
    begin=0
    while i<len(opts):
        if opts[i]==1:
            begin=(begin+1)%len(nums)
            i+=1
        elif opts[i]==2:
            opt2_nums=0
            while i<len(opts) and opts[i]==2:
                opt2_nums+=1
                i+=1
            if opt2_nums%2==1:
                opt2(nums,begin)
    return nums,begin


# N,M=[int(x) for x in sys.stdin.readline().strip().split(' ')]
# opts=[int(x) for x in sys.stdin.readline().strip().split(' ')]
# result=solve(N,opts)
# print(' '.join(max(str,result)))

if __name__ == '__main__':
    import random
    opts=[random.randint(1,2) for _ in range(10000)]
    result,begin = solve(10000, opts)
    nums=result[begin:]+result[:begin]
    print(' '.join(map(str, nums)))
