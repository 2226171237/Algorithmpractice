#-*-coding=utf-8-*-

'''
如何求出数组中绝对值最小的数
有一个升序排列的数组，数组中可能有正数，负数，0，求数组中元素的绝对值最小的数。
如[-10,-5,-2,7,15,50]
绝对值最小的数为-2
'''
# 顺序比较法
def findMinAbs1(arr):
    Min=arr[0]
    for x in arr:
        if abs(x)<abs(Min):
            Min=x
    return Min

# 二分法,递归
def findMinAbs2(arr,begin,end):
    if begin>=end:
        return arr[begin]
    if arr[end-1]<=0:
        return arr[end-1]
    if arr[begin]>=0:
        return arr[begin]
    mid=(begin+end)//2
    x=findMinAbs2(arr,begin,mid)
    y=findMinAbs2(arr,mid,end)
    if abs(x)<abs(y):
        return x
    else:
        return y
# 二分法 O(logN)
def findMinAbs3(arr):
    begin=0
    end=len(arr)
    while begin<end:
        mid = (begin + end) // 2
        if arr[mid]==0:
            return 0
        if arr[mid]>0:
            if arr[mid-1]<0:
                return arr[mid] if abs(arr[mid])<abs(arr[mid-1]) else arr[mid-1]
            else:
                end=mid
        else:
            if mid+1>=len(arr):
                return arr[mid]
            if arr[mid+1]>0:
                return arr[mid] if abs(arr[mid]) < abs(arr[mid + 1]) else arr[mid + 1]
            else:
                begin=mid+1
    if begin==end:
        return arr[begin]

if __name__ == '__main__':
    arr=[-10,-8,-5,9,10,12,12]
    print(findMinAbs1(arr))
    print(findMinAbs2(arr,0,len(arr)))
    print(findMinAbs3(arr))