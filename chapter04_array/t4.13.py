#-*-coding=utf-8 -*-
'''
如何在不排序的情况下求数组的中位数？
'''

# 如果没有排序限制，先使用快速排序算法。
def getMid1(arr):

    def qsorted(arr):
        if len(arr)<2:
            return arr
        base=arr[0]
        left=[x for x in arr[1:] if x<base]
        right=[x for x in arr[1:] if x>=base]
        return qsorted(left)+[base]+qsorted(right)

    arr=qsorted(arr)
    mid=len(arr)//2
    if len(arr)%2:
        return arr[mid]
    else:
        return (arr[mid]+arr[mid-1])/2

# 类快速排序

# 快排，根据基值，分数组。
def partition(arr,low,high):
    key=arr[low]
    while low<high:
        while low<high and arr[high]<key:
            high-=1
        arr[low]=arr[high]

        while low<high and arr[low]>key:
            low+=1
        arr[high]=arr[low]
    arr[low]=key
    return low

def getMid2(arr):
    low=0
    high=len(arr)-1
    n=len(arr)
    mid=(low+high)//2
    while True:
        p=partition(arr,low,high)
        if p==mid:
            break
        elif p>mid:
            high=p-1
        else:
            low=p+1

    return arr[mid] if (n%2) else (arr[mid]+arr[mid+ 1])/2

if __name__ == '__main__':
    arr=[7,5,3,1,11,9,8,5]
    print(getMid1(arr))
    print(getMid2(arr))
    print(arr)
