'''
直接基数排序法
'''
from collections import deque

def straight_radix(X):
    if len(X)<=1:
        return X
    n=1
    maxnum=max(X)
    while maxnum>10**n:
        n+=1
    Q=[deque() for _ in range(10)]
    for i in range(n):
        for x in X:
            d=int((x//(10**i))%10)
            Q[d].append(x)
        j=0
        for t in range(10):
            while len(Q[t]):
                X[j]=Q[t].popleft()
                j+=1
    return X


if __name__ == '__main__':
    import random
    X=[random.randint(0,30) for _ in range(40)]
    print(X)
    print(straight_radix(X))