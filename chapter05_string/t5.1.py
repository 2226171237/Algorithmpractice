# -*-coding=utf-8 -*-
'''
如何求一个字符串的所有排列？
设计一个程序，当1输入一个字符串时，要求输出这个字符串的所有排列。
如：输入 abc，输出： abc,acb,bca,bac,cab,cba
'''

# 方法1：递归
def permutation(s,start):
    if not isinstance(s,list):
        s=list(s)
    if start==len(s)-1:
        print(''.join(s))
        return
    i=start
    while i<len(s):
        tmp=s[start]
        s[start]=s[i]
        s[i]=tmp
        permutation(s,start+1)
        i+=1

# 非递归
def getSub(s):
    p1=len(s)-1
    p2=p1-1
    while p2>=0:
        if s[p1]>s[p2]:
            return p2
        else:
            p1-=1
            p2-=1
    return -1

def getMax(s,ind):
    m=ind+1
    i=ind+1
    min=s[i]
    while i<len(s):
        if s[i]>s[ind] and min>s[i]:
            min=s[i]
            m=i
        i+=1
    return m

def swap(s,i,j):
    tmp=s[i]
    s[i]=s[j]
    s[j]=tmp

def transpose(s,ind):
    low=ind+1
    high=len(s)-1
    while low<high:
        swap(s,low,high)
        low+=1
        high-=1

def permutation2(s):
    s=list(s)
    s=sorted(s)
    print(''.join(s))
    ind=getSub(s)
    while ind>=0:
        m=getMax(s,ind)
        swap(s,ind,m)
        transpose(s,ind)
        print(''.join(s))
        ind=getSub(s)

if __name__ == '__main__':
    permutation2('1234567')
