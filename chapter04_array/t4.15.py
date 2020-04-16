# -*-coding=utf-8 -*-
'''
如何对数组进行循环移位？
把一个包含N个元素的数组循环右移K(K是正数)位，要求时间复杂度位O(N),且只允许使用两个附加变量。
'''

# 方法1：蛮力法，依次移动K次

def rightShift1(array,k):
    k=k%len(array)
    for _ in range(k):
        # 向右移动一位
        tmp=array[-1]
        i=len(array)-1
        while i>0:
            array[i]=array[i-1]
            i-=1
        array[0]=tmp

# 方法2：反转法
def transposeArray(array,low,high):
    # 将数组进行倒置
    while low <high:
        tmp=array[low]
        array[low]=array[high]
        array[high]=tmp
        low+=1
        high-=1

def rightShift2(array,k):
    k=k%len(array)
    lens=len(array)
    transposeArray(array,0,lens-k-1)
    transposeArray(array,lens-k,lens-1)
    transposeArray(array,0,lens-1)

if __name__ == '__main__':
    arr=[1,2,3,4,5,6]
    rightShift1(arr,8)
    print(arr)

    arr = [1, 2, 3, 4, 5, 6]
    rightShift2(arr, 8)
    print(arr)