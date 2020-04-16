'''
如何求最长递增子序列的长度？
假设L=<a1,a2,...,an>是n个不同的实数的序列，L的递增子序列是这样一个子序列，
Lin=<ak1,ak2,...,akm>,其中 k1<k2<...<km且ak1<ak2<...<akm。求最大的m值。
'''
# 递归法
def getMaxAscendingLen1(s):
    if len(s)<=1:
        return len(s)
    i=0
    j=1
    while j<len(s) and s[j]>s[i]:
        i+=1
        j+=1
    next_len=getMaxAscendingLen1(s[j:])
    if j>next_len:
        return j
    else:
        return next_len

#归纳假设法(动态规划)
def getMaxAscendingLen2(s):
    result=[0 for _ in range(len(s))]
    result[0]=1
    j=0 # 最长递增子序列的最后一个坐标
    m=1 # 最长递增后序长度
    i=1
    while i<len(s):
        if j==i-1:
            if s[i]>=s[j]:
                result[i]=result[i-1]+1
                j=i
                m=result[i]
            else:
                m=1
                result[i]=result[i-1]
        else:
            if s[i]>=s[i-1]:
                m+=1
                if result[i-1]<=m:
                    result[i]=m
                    j=i
                else:
                    result[i]=result[i-1]
            else:
                m=1
                result[i]=result[i-1]
        i+=1
    print(result)
    return result[-1]


# 最长公共子序列，相对原序列进行递增排序，然后求与原序列的最长公共子序列。
# 只适合递增时元素差值<=1情形。
def qsort(L):
    if len(L)<=1:
        return L
    base=L[0]
    left=[x for x in L[1:] if x <base]
    right=[x for x in L[1:] if x>=base]
    return qsort(''.join(left))+base+qsort(''.join(right))

def getMaxAscendingLen3(s):
    # 先排序
    LO=qsort(s)

    # 求最长公共子串，动态规划法
    M=[[0 for _ in range(len(s)+1)] for _ in range(len(s)+1) ]
    i=1
    maxs=0
    while i<len(s)+1:
        j=1
        while j<len(s)+1:
            if s[i-1]==LO[j-1]:
                M[i][j]=M[i-1][j-1]+1
                if M[i][j]>maxs:
                    maxs=M[i][j]
            else:
                M[i][j]=0
            j+=1
        i+=1
    return maxs+1


if __name__ == '__main__':
    s='xbcdfzacdefghijqasdh'
    print(getMaxAscendingLen1(s))
    print(getMaxAscendingLen2(s))
    print(getMaxAscendingLen3(s))