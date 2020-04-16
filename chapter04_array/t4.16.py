# -*-coding=utf-8 -*-
'''
如何在有规律的二维数组中进行高校的数据查找？
在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请实现一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数？
'''
# 只在行傻瓜使用有序性
def binSerach(arr,low,high,num):
    if low>high:
        return False
    mid=(low+high)//2
    if arr[mid]==num:
        return True
    elif arr[mid]>num:
        return binSerach(arr,low,mid-1,num)
    else:
        return  binSerach(arr,mid+1,high,num)

def findNum(arr,num):
    i=0
    while i<len(arr):
        if arr[i][-1]>num:
            result=binSerach(arr[i],0,len(arr[i])-1,num)
            if result:
                return result
        elif arr[i][-1]==num:
            return True
        i+=1
    return False

# 行列都使用有序性,每次过滤掉一行或一列。
def findNum2(arr,num):
    i=0
    j=len(arr[0])-1
    while i<len(arr) and j>=0:
        if arr[i][j]==num:
            return True
        elif arr[i][j]<num:
            i+=1
        else:
            j-=1
    return False

if __name__ == '__main__':
    arr=[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
    print(findNum(arr,6))
    print(findNum2(arr, 6))