#-*-coding=utf-8 -*-
'''
如何找出数组中出现一次的数？
一个数组里，除了三个数是唯一出现，其余的数都是偶数次，找出这三个数中的任意一个。
如 [1，2，4，5，6，4，2] 只有1，5，6这三个数唯一出现，只输出1，5，6中一个即可。
'''

# 哈希字典
def findNum1(arr):
    hash_dict=dict()
    for x in arr:
        if x in hash_dict:
            hash_dict[x]+=1
        else:
            hash_dict[x]=0
    for x in hash_dict:
        if hash_dict[x]==0:
            return x

# 找三个数中不同的bit位
def findNum2(arr):
    i=0
    while i<32:
        result0 = 0
        result1 = 0
        count0 = 0
        count1 = 0
        for x in arr:
            if (x>>i)&1:
                result1^=x
                count1+=1
            else:
                result0^=x
                count0+=1
        if result0!=0 and count0%2:
            return result0
        if result1!=0 and count1%2:
            return result1

if __name__ == '__main__':
    arr=[1,2,4,5,6,4,2]
    print(findNum1(arr))
    print(findNum2(arr))