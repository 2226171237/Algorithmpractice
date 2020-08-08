import unittest


def getLongest(s):
    n=len(s)
    dp=[[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dp[i][i]=1
    for i in range(n-1):
        if s[i]==s[i+1]:
            dp[i][i+1]=2
        else:
            dp[i][i+1]=1
    for jj in range(2,n):
        for i in range(0,n-jj):
            j=i+jj
            if s[i]==s[j]:
                if dp[i+1][j-1]==1:
                    dp[i][j]=2
                else:
                    dp[i][j]=dp[i+1][j-1]+2
            else:
                dp[i][j]=max(dp[i][j-1],dp[i+1][j])
    return dp[0][n-1]

print(getLongest('abcfceefea'))