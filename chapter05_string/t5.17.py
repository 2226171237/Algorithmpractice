'''
如何求解字符串中字典序最大的子序列。
给定一个字符串，求串中字典序最大的子序列。字典序最大的子序列是这样构造的：给定字符串a0,a1,a2,..,an-1
首先在字符串a0,a1,a2,..,an-1中找到值最大的字符ai,然后再剩余的字符串ai+1,...,an-1中找到值最大的字符aj，
依次类推，直到字符串长度为0。
'''

def getMax(L):
    maxs=L[0]
    maxsI=0
    i=1
    while i<len(L):
        if L[i]!='':
            if L[i]>maxs:
                maxs=L[i]
                maxsI=i
        i+=1
    return maxs,maxsI

def getMaxSubStr1(s):
    n=len(s)
    L=list(s)
    sb=''
    i=0
    j=0
    while i<len(s):
        x,next_j=getMax(L[j:])
        if x=='':
            break
        sb+=x
        j=j+next_j
        L[j]=''
        i+=1
    return sb

# 逆序遍历
def getMaxSubStr2(s):
    n=len(s)
    i=n-2
    sb=[s[-1]]
    while i>=0:
        if s[i]>=sb[-1]:
            sb.append(s[i])
        i-=1
    return ''.join(sb[::-1])

if __name__ == '__main__':
    s='acbdxmng'
    print(getMaxSubStr1(s))
    print(getMaxSubStr2(s))
