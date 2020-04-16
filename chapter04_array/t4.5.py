#-*-coding=utf-8-*-
'''
如何找出数组中出现奇数次的数？
数组中有N+2个数，其中N个数出现了偶数次，2个数出现了奇数次(这两个数不相等)
请用O(1)的空间复杂度，找出这两个数。
'''

def findNums(arr):
    xor=0
    for x in arr:
        xor^=x
    position=0
    while (xor>>position)&1==0:
        position+=1
    a=0
    for x in arr:
        if (x>>position)&1:
            a^=x
    return a,xor^a
if __name__ == '__main__':
    arr=[3,5,6,6,5,7,2,2,5,5,3,7,5,3]
    print(findNums(arr))