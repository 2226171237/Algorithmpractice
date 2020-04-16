'''
直接基数排序法
'''
from collections import deque

def getBitNum(num,k):
    # 返回十进制数的第k位
    nums=[]
    while num:
        nums.append(num%10)
        num=num//10
    K=len(nums)
    return nums[K-k]

def straight_radix(X,n,k):
    Q=[deque() for _ in range(10)]
    for i in range(k,0,-1):
        for x in X:
            d=getBitNum(x,i)
            Q[d].append(x)
        j=0
        for t in range(10):
            while len(Q[t]):
                X[j]=Q[t].popleft()
                j+=1
    return X


if __name__ == '__main__':
    import random
    X=[random.randint(10,30) for _ in range(40)]
    print(X)
    print(straight_radix(X,1,2))
