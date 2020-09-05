

def longestComSubSeq(str1,str2):
    n1=len(str1)
    n2=len(str2)
    if 0==n1 or 0==n2:
        return 0
    dp=[[0 for _ in range(n2+1)] for _ in range(n1+1)]
    for i in range(1,n1+1):
        for j in range(n2+1):
            if str1[i-1]==str2[j-1]:
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j]=max(dp[i][j-1],dp[i-1][j])
    return dp[-1][-1]

print(longestComSubSeq('abcde','ace'))