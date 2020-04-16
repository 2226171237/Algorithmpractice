'''
求一个串中出现的第一个最长重复子串。
给定一个字符串，找出这个字符串中最长的重复子串，比如给定字符串'banana',字符串'ana'出现了两次，因此最长重复子串
为'ana'
'''

def partition(L,low,high):
    base=L[low]
    while low<high:
        while low<high and L[high]>=base:
            high-=1
        L[low]=L[high]
        while low<high and L[low]<base:
            low+=1
        L[high]=L[low]
    L[low]=base
    return low

def qsort(L,low,high):
    if low>=high:
        return
    ind=partition(L,low,high)
    qsort(L,low,ind-1)
    qsort(L,ind+1,high)


def getComLen(s1,s2):
    # 最长公共前缀
    i=0
    n1=len(s1)
    n2=len(s2)
    m=0
    while i<n1 and i<n2:
        if s1[i]==s2[i]:
            m+=1
            i+=1
        else:
            break
    return m

# 后缀数组法
def getMaxCommonStr1(s):
    # 取后缀字符串，并排序
    L=[]
    i=0
    n=len(s)
    while i<n:
        L.append(s[i:])
        i+=1
    qsort(L,0,n-1)
    # 比较相邻字符串的最长公共串
    maxLen=1
    sb=''
    i=0
    while i<len(L)-1:
        lens=getComLen(L[i],L[i+1])
        if lens>maxLen:
            maxLen=lens
            sb=L[i][:maxLen]
        i+=1
    return sb

if __name__ == '__main__':
    s='bananan'
    print(getMaxCommonStr1(s))