#-*-coding=utf-8-*-
'''
如何找出旋转数组的最小元素？
把一个有序数组最开始的若干个元素搬到数组的末尾，称之为数组的旋转。输入一个排好序的数组的一个旋转，
输出旋转数组的最小元素。如：[3,4,5,1,2]为数组[1,2,3,4,5]的一个旋转，该数组最小值为1.
'''

def findMin1(arr,low,high):
    if high<low:
        return arr[0]
    if high==low:
        return arr[low]
    mid=low+((high-low)>>1)   #(low+high)//2
    if arr[mid]<arr[mid-1]:
        return arr[mid]
    elif arr[mid]>arr[mid+1]:
        return arr[mid+1]
    elif arr[high]>arr[mid]:
        return findMin1(arr,low,mid-1)
    elif arr[mid]>arr[low]:
        return findMin1(arr,mid+1,high)
    else:
        return min(findMin1(arr,low,mid-1),findMin1(arr,mid+1,high))

# 引申：实现旋转数组功能
def swap(arr,low,high):
    while low<high:
        tmp=arr[low]
        arr[low]=arr[high]
        arr[high]=tmp
        low+=1
        high-=1

def rotateArr(arr,div):
    if 0==div:
        return
    swap(arr,0,div-1)
    swap(arr,div,len(arr)-1)
    swap(arr,0,len(arr)-1)

if __name__ == '__main__':
    arr=[1,2,3,4,5,6]
    print(findMin1(arr,0,len(arr)-1))
    rotateArr(arr,3)
    print(arr)