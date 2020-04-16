'''
如何求两个字符串的最长公共子串。
'''

def getMaxSubStr1(s1,s2):
    n1=len(s1)
    n2=len(s2)
    i=0
    subStr=''
    while i<n1:
        s=''
        j=0
        k = 0
        while j<n2:
            if i+k<n1 and s1[i+k]==s2[j]:
                s+=s1[i+k]
                k+=1
            else:
                if k>len(subStr):
                    subStr=s
                s=''
                j-=k
                k=0
            j+=1
        if k >len(subStr):
            subStr = s
        i+=1

    return subStr

# 动态规划
def getMaxSubStr2(s1,s2):
    n1=len(s1)
    n2=len(s2)
    sb=''
    maxs=0
    maxI=0
    M=[[0 for _ in range(n2+1)] for _ in range(n1+1)]
    i=1
    while i<n1+1:
        j=1
        while j<n2+1:
            if s1[i-1]==s2[j-1]:
                M[i][j]=M[i-1][j-1]+1
                if M[i][j]>maxs:
                    maxs=M[i][j]
                    maxI=i
            else:
                M[i][j]=0
            j+=1
        i+=1
    i=maxI-maxs
    while i<maxI:
        sb+=s1[i]
        i+=1
    return sb



if __name__ == '__main__':
    s1='abccaddefgcfgcdeaeahs1234567isasa'
    s2='dgcadddefgaefgcdeaeasha1234567isaia'
    print(getMaxSubStr1(s1,s2))
    print(getMaxSubStr2(s1,s2))
