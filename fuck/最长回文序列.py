

#  问题1： 最长回文子串
def maxLen(s,i,j):
    while i>=0 and j<len(s) and s[i]==s[j]:
        i-=1
        j+=1
    return j-i-1

def longestHuiwenSubStr1(s):
    maxL=1
    for i in range(len(s)):
        maxL=max(maxL,maxLen(s,i,i),maxLen(s,i,i+1))
    return maxL

def longestHuiwenSubstr2(s):
    N=len(s)
    if N==0:
        return 0
    maxL=1
    DP=[[False for _ in range(N)] for _ in range(N)]
    for i in range(N):
        DP[i][i]=True
        if i<N-1 and s[i]==s[i+1]:
            DP[i][i+1]=True
    for jj in range(2,N):
        for i in range(0,N-jj):
            j=i+jj
            DP[i][j]=DP[i+1][j-1] and s[i]==s[j]
            if DP[i][j]:
                maxL=max(maxL,j-i+1)
    return maxL

print(longestHuiwenSubStr1('aedsbzxyxzbaba'))
print(longestHuiwenSubstr2('aedsbzxyxzbaba'))

# 问题2：最长回文子序问题
def longestHuiwenSubSeq(s):
    N=len(s)
    if 0==N:
        return 0
    DP=[[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        DP[i][i]=1
        if i<N-1:
            DP[i][i+1]=2 if s[i]==s[i+1] else 1

    for jj in range(2,N):
        for i in range(0,N-jj):
            j=i+jj
            if s[i]==s[j]:
                DP[i][j]=2+DP[i+1][j-1]
            else:
                DP[i][j]=max(DP[i+1][j],DP[i][j-1])
    return DP[0][-1]

print(longestHuiwenSubSeq('xyzaxzsey'))