# -*-coding=utf-8 -*-
'''
如何求两个有序集合的交集？
右两个有序集合，集合中的每个元素都是一段范围，求其交集。
例如集合{[4,8],[9,13]}和集合{[6,12]}的交集为{[6,8],[9,12]}
'''

# 交替法
def getComSet(arr1,arr2):
    result=[]
    i=0
    j=0
    n1=len(arr1)
    n2=len(arr2)
    while i<n1 and j<n2:
        s1=arr1[i]
        s2=arr2[j]
        a=max(s1[0],s2[0])
        b=min(s1[1],s2[1])
        if b>a:
            result.append([a,b])
            if (s1[0]<s2[1]<s1[1]) or (s2[0]>s1[0] and s2[1]<s1[1]):
                j+=1
            else:
                i+=1
        else:
            if s1[1]<s2[0]:
                i+=1
            elif s2[1]<s1[0]:
                j+=1

    return result

if __name__ == '__main__':
    arr1=[[4,8],[9,13],[14,15],[17,20]]
    arr2=[[6,12],[13.5,15],[18,19]]
    print(getComSet(arr1,arr2))