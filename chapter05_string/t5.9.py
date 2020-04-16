'''
如何实现字符串的匹配？
给定主字符串S,与模式字符串P，判断P是否是S的子串，如果是，那么找出P在S中第一次出现的位置
'''

# 方法1：直接比较法
def find(S,P):
    ns=len(S)
    np=len(P)
    i = 0
    while i<ns:
        if ns-i<np:
            return -1
        j=0
        while j<np and P[j]==S[i+j]:
            j+=1
        if j==np:
            return i
        i+=1
    return -1

# 方法2：KMP算法
def getMax(s):
    '''最大长度前后缀'''
    high=len(s)-1
    counts=0
    k=1
    while k<=high:
        j=0
        while high-k+1+j<=high and s[j]==s[high-k+1+j]:
            j+=1
        if j==k:
            counts=k
        k+=1
    return counts

def getNexts(P):
    next=[0 for _  in range(len(P))]
    i=1
    n=len(P)
    while i<n:
        next_j=getMax(P[0:i+1])
        next[i]=next_j
        i+=1
    return next

def find_kmp(S,P):
    next=getNexts(P)
    i=0
    n=len(S)
    j=0
    while i<n:
        if S[i]==P[j]:
            j+=1
            i+=1
            if j>=len(P):
                break
        else:
            j=next[j]
            if j==0:
                i+=1
    if j==len(P):
        return i-j
    else:
        return -1

if __name__ == '__main__':
    s='ababaaaba'
    p='abaa'
    print(find(s,p))
    print(find_kmp(s,p))
    