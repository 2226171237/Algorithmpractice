#-*-coding=utf-8-*-
'''
如何求数组连续的最大和？
一个有n个元素的数组，这n个元素既可以是正数也可以是负数，数组中来纳许的一个或多个元素
可以组成一个连续的子数组，一个数组可能有多个这样来的连续的子数组，求子数组和的最大值。
如：[4,8,-4,7] 最大值为15
'''

# 蛮力法
def maxSumArray1(arr):
    subLen=0
    maxSum=arr[0]
    while subLen<=len(arr):
        i=0
        while i<=len(arr)-subLen:
            j=0
            sum=0
            while j<subLen:
                sum+=arr[j+i]
                j+=1
            if sum>maxSum:
                maxSum=sum

            i+=1
        subLen+=1

    return maxSum

# 重复利用已经计算的子数组和
def maxSumArray2(arr):
    maxSum=arr[0]
    i=0
    while i<len(arr):
        j=i
        sum=0
        while j<len(arr):
            sum+=arr[j]
            if sum>maxSum:
                maxSum=sum
            j+=1
        i+=1
    return maxSum

# 动态规划方法
def maxSumArray3(arr):
    lens=len(arr)
    End=[None for _ in range(lens)]
    All=[None for _ in range(lens)]
    End[-1]=arr[-1]
    All[-1]=arr[-1]
    End[0]=arr[0]
    All[0]=arr[0]

    i=1
    while i<lens:
        End[i]=max(End[i-1]+arr[i],arr[i])
        All[i]=max(End[i],All[i-1])
        i+=1
    return All[-1]

# 优化的动态规划
def maxSumArray4(arr):
    lens=len(arr)
    End=arr[0]
    All=arr[0]

    i=1
    while i<lens:
        End=max(End+arr[i],arr[i])
        All=max(End,All)
        i+=1
    return All

if __name__ == '__main__':
    arr=[1,-2,4,8,-4,7,-1,-5]
    print(maxSumArray1(arr))
    print(maxSumArray2(arr))
    print(maxSumArray3(arr))
    print(maxSumArray4(arr))