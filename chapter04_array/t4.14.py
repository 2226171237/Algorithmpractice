# -*-coding=utf-8 -*-
'''
如何求集合的所有子集。
有一个集合，求其全部子集（包含集合自身）。给定一个集合S，它包含两个元素<a,b>,则其全部子集为：
<a,ab,b>
'''

# 方法1：位图法

def getAllSubSet1(array,mask,c):
    length=len(array)
    if length==c:
        print('{',end='')
        i=0
        while i<length:
            if mask[i]==1:
                print(array[i],end=' ')
            i+=1
        print('}')
    else:
        mask[c]=1
        getAllSubSet1(array,mask,c+1)
        mask[c]=0
        getAllSubSet1(array,mask,c+1)

# 方法2：迭代法
def getAllSubSet2(array):
    allSubSet=[]
    allSubSet.append(array[0:1])
    for x in array[1:]:
        subLens=len(allSubSet)
        i=0
        while i<subLens:
            allSubSet.append(allSubSet[i]+x)
            i+=1
        allSubSet.append(x)
    return allSubSet

if __name__ == '__main__':
    array=['a','b','c']
    mask=[0,0,0]
    getAllSubSet1(array,mask,0)

    result=getAllSubSet2('abc')
    print(result)
