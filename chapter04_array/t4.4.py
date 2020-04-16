#-*-coding=utf-8-*-
'''
如何找出数组中丢失的数？
给定一个由n-1个整数组成的未排序数组序列，其元素都是1到n之间的不同的整数。请写出一个寻找数组序列中缺失整数的
线性时间算法。
'''

def findNum1(arr):
    # 累加法
    sum=0
    for i,x in enumerate(arr):
        sum+=x

    return (1+len(arr)+1)*(len(arr)+1)/2-sum

def findNum2(arr):
    # 异或法：
    xor=0
    for i,x in enumerate(arr):
        xor^=x
        xor^=i+1
    xor^=len(arr)+1
    return xor

if __name__ == '__main__':
    arr=[1,4,3,2,7,5]
    print(findNum1(arr))
    print(findNum2(arr))