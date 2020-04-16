# -*-coding=utf-8 -*-
'''
如何判断请求能否在给的存储条件下完成。
给定一台有m个存储空间的机器，有n个请求需要在这台机器上运行，第i个请求计算时需要占R[i]空间，
计算结果需要占O[i]个空间(O[i]<R[i])。请设计一个算法，判断这n个请求能否全部完成？若能，给出这n个请求的安排顺序。
'''

def partition(arr,arg_arr,low,high):
    base=arr[low]
    arg_low=arg_arr[low]
    while low<high:
        while low<high and arr[high]<=base:
            high-=1
        arr[low]=arr[high]
        arg_arr[low]=high
        while low<high and arr[low]>=base:
            low+=1
        arr[high]=arr[low]
        arg_arr[high]=low
    arr[low]=base
    arg_arr[low]=arg_low
    return low

def qsort(arr,arg_arr,low,high):
    if low>=high:
        return
    index=partition(arr,arg_arr,low,high)
    qsort(arr,arg_arr,low,index-1)
    qsort(arr,arg_arr,index+1,high)

# 方法1：
def schedule(R,O,m):
    result=[]
    i=0
    n=len(R)
    while i<n:
        result.append(R[i]-O[i])
        i+=1
    arg_result=list(range(n))
    qsort(result,arg_result,0,n-1)
    for i in arg_result:
        if m>R[i]:
            m-=O[i]
        else:
            return False
    return arg_result

if __name__ == '__main__':
    R=[10,15,23,20,6,9,7,16]
    O=[2,7,8,4,5,8,6,8]
    result=schedule(R,O,50)
    if result:
        print(result)

