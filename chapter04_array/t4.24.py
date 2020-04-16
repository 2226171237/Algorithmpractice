# -*-coding=utf-8 -*-
'''
如何对有大量重复的数字的数组进行排序？
给定一个数组，已知这个数组中有大量的重复数组，如何对这个数组进行高效的排序？
'''
# 方法1：快速排序
def partition(arr,low,high):
    base=arr[low]
    while low<high:
        while high>low and arr[high]>=base:
            high-=1
        arr[low]=arr[high]
        while high>low and arr[low]<=base:
            low+=1
        arr[high]=arr[low]
    arr[low]=base
    return low

def qsort(arr,low,high):
    if low>=high:
        return
    ind=partition(arr,low,high)
    qsort(arr,low,ind-1)
    qsort(arr,ind+1,high)


# 方法2： AVL数 平衡二叉树，然后中序遍历

# 方法3：哈希法
def sortArr(arr):
    hash_d=dict()
    for x in arr:
        if x in hash_d:
            hash_d[x]+=1
        else:
            hash_d[x]=1
    i=0
    for key in sorted(hash_d.keys()):
        while hash_d[key]>0:
            arr[i]=key
            i+=1
            hash_d[key]-=1
    return arr
if __name__ == '__main__':
    arr=[1,2,3,6,4,7,8,9,4,6,7]
    qsort(arr,0,10)
    print(arr)

    arr=sortArr([15,12,15,2,2,12,2,3,12,100,3,3])
    print(arr)