# coding=utf-8 -*-
'''
如何寻找最多的覆盖点？
坐标轴上从左到右依次的点为a[0],a[1],a[2],...,a[n-1],设一根木棒的长度为L，
求L最多覆盖坐标的几个点？
'''

# 暴力法
def converNum(arr,L):
    maxCounts=0
    for i,x in enumerate(arr):
        counts=0
        for y in arr[i:]:
            if y<=L+x:
                counts+=1
            else:
                break
        if counts>maxCounts:
            maxCounts=counts
    return maxCounts


def converNum2(arr,L):
    maxCounts=1
    i=0
    j=1
    n=len(arr)
    while i<n and j<n:
        while j<n and arr[j]-arr[i]<=L:
            j+=1
        j-=1
        if maxCounts<j-i+1:
            maxCounts=j-i+1
        i+=1
    return maxCounts
if __name__ == '__main__':
    a=[1,3,7,8,10,11,12,13,15,16,17,19,25]
    print(converNum(a,7))
    print(converNum2(a, 7))