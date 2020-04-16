#-*-coding=utf-8-*-
'''
如何查找数组中元素的最大值和最小值？
给定数组a1,a2,a3,...an,要求找出数组的最大值和最小值。假设数组中的值两两各不相同。
'''
def findMaxAndMin1(arr):
    # 蛮力法
    if None==arr:
        return None,None
    max,min=arr[0],arr[0]
    for x in arr[1:]:
        if x>max:
            max=x
        if x<min:
            min=x
    return max,min

def findMaxAndMin2(arr):
    # 分治法
    if None==arr:
        return None,None
    max,min=arr[0],arr[0]
    lens=len(arr)
    i=0
    while i<lens-1:
        if arr[i]>arr[i+1]:
            tmp=arr[i]
            arr[i]=arr[i+1]
            arr[i+1]=tmp
        i+=2
    i=0
    while i<lens-1:
        if arr[i]<min:
            min=arr[i]
        i+=2
    j=1
    while j<lens:
        if arr[j]>max:
            max=arr[j]
        j+=2
    if lens%2:
        if min>arr[-1]:
            min=arr[-1]
        if max<arr[-1]:
            max=arr[-1]
    return max,min

def findMaxAndMin3(arr,l,r):
    # 变形的分治法,递归
    if l>=r:
        return arr[l],arr[l]
    mid=(l+r)//2
    leftmax,leftmin=findMaxAndMin3(arr,l,mid)
    rightmax,rightmin=findMaxAndMin3(arr,mid+1,r)
    Max=max(leftmax,rightmax)
    Min=min(leftmin,rightmin)
    return Max,Min

if __name__ == '__main__':
    import random
    arr=[1,2,3,47,8,9,8,9,100,23,221,89,0]
    random.shuffle(arr)
    print(arr)
    print(findMaxAndMin1(arr))
    print(findMaxAndMin2(arr))
    print(findMaxAndMin3(arr,0,len(arr)-1))
