'''
给定一个数组序列, 需要求选出一个区间, 使得该区间是所有区间中经过如下计算的值最大的一个：
区间中的最小数 * 区间所有数的和最后程序输出经过计算后的最大值即可，不需要输出具体的区间。如给定序列[6
2 1]则根据上述公式, 可得到所有可以选定各个区间的计算值:
[6] = 6 * 6 = 36;
[2] = 2 * 2 = 4;
[1] = 1 * 1 = 1;
[6, 2] = 2 * 8 = 16;
[2, 1] = 1 * 3 = 3;
[6, 2, 1] = 1 * 9 = 9;
从上述计算可见选定区间[6] ，计算值为
36， 则程序输出为
36。
区间内的所有数字都在[0, 100]
的范围内;
'''

# 暴力法
def solver1(L):
    mins=L[0]
    s=L[0]
    maxS=mins*s
    i=0
    n=len(L)
    while i<n:

        mins=L[i]
        s=L[i]
        if mins*s>maxS:
            maxS=mins*s
        j=i+1
        while j<n:
            if L[j]<mins:
                mins=L[j]
            s+=L[j]
            if mins*s>maxS:
                maxS=mins*s
            j+=1
        i+=1
    return maxS


# 动态规划法
def solver2(L):
    n=len(L)
    min1=L[0]
    s1=L[0]
    j=0 # 区间的最后一个元素索引
    min2=L[0]
    s2=L[0]
    maxS=min1*s1
    i=1
    while i<n:
        if i-1==j:
            t=min1 if min1<L[i] else L[i]
            if t*(s1+L[i])>maxS:
                s1+=L[i]
                j=i
                min1=t
                maxS=min1*s1
        else:
            t=min2 if L[i]>min2 else L[i]
            if t*(s2+L[i])>maxS:
                min2=t
                s2+=L[i]
                maxS=min2*s2
                min1=min2
                s1=s2
                j=i

        k = i - 1
        min2 = L[i]
        s2 = L[i]
        maxT = min2 * s2
        while k >= 0:
            t = min2 if L[k] > min2 else L[k]
            if t * (s2 + L[k]) > maxT:
                min2 = t
                s2 += L[k]
                maxT = min2 * s2
            else:
                break
            k -= 1
        if maxT > maxS:
            maxS = maxT
            min1 = min2
            s1 = s2
            j = i

        i+=1
    return maxS

# 中心扩展法，以第i个元素为最小值分别向两边扩大区间至最大，算出该元素与区间内所有数的和的
# 乘积f(i)，遍历所有元素，更新f(i)即可。

def solver3(L):
    n=len(L)
    i=0
    maxS=L[0]*L[0]
    while i<n:
        s=0
        j=i
        while j>=0 and L[j]>=L[i]:
           s+=L[j]
           j-=1
        j=i
        while j<n and L[j]>=L[i]:
            s+=L[j]
            j+=1
        s-=L[i]
        if maxS<s*L[i]:
            maxS=s*L[i]
        i+=1
    return maxS

# leetcode84 Largest Rectangle in Histogram And 85. Maximal Rectangle
def solver4(L):
    Stack=[L[0]]
    SumStack=[L[0]]
    n=len(L)
    i=1
    maxS=L[0]*L[0]
    while i<n:
        top=Stack[-1]
        mins=top
        s=0
        while top>L[i] and len(Stack):
            Stack.pop()
            s+=top+SumStack.pop()
            if mins>top:
                mins=top
            maxS=max(mins*s,maxS)
            if len(Stack):
                top=Stack[-1]
            else:
                break
        Stack.append(L[i])
        SumStack.append(s)
        i+=1
    return maxS

if __name__ == '__main__':
    import random
    import time

    L=list(range(20000))
    LS=[]
    NUMS=1000
    for _ in range(NUMS):
        random.shuffle(L)
        LS.append(L[:])
    random.shuffle(L)
    print(solver1(L))
    print(solver2(L))
    print(solver3(L))
    print(solver4(L))
    t=time.time()
    for i in range(NUMS):
        #solver1(LS[i])
        pass

    print(time.time()-t)

    t = time.time()
    for i in range(NUMS):
        solver2(LS[i])
    print(time.time() - t)

    t = time.time()
    for i in range(NUMS):
        solver3(LS[i])
    print(time.time() - t)

    t = time.time()
    for i in range(NUMS):
        solver4(LS[i])
    print(time.time() - t)