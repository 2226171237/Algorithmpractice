# -*-coding=utf-8 -*-
'''
如何从三个有序的数组中找出它们的公共元素？
给定以非递减顺序的三个数组，找出这三个数组中的所有公共元素。
'''

def getCoNums(arr1,arr2,arr3):
    i=0
    j=0
    k=0
    result=[]
    while i<len(arr1) and j<len(arr2) and k<len(arr3):
        if arr1[i]==arr2[j] and arr2[j]==arr3[k]:
            result.append(arr1[i])
            i+=1
            j+=1
            k+=1
        elif arr1[i]<arr2[j]:
            i+=1
        elif arr2[j]<arr3[k]:
            j+=1
        else:
            k+=1
    return result


if __name__ == '__main__':

    arr1=[1,3,5,6,8,10,12]
    arr2=[3,5,9,10,11,13,14]
    arr3=[5,6,7,8,9,10,11]
    print(getCoNums(arr1,arr2,arr3))