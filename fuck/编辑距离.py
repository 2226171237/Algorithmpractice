

def editDistance(s1,s2):
    '''
    动态规划；
    :param s1:
    :param s2:
    :return:
    '''
    n1=len(s1)
    n2=len(s2)
    dp=[[0 for _ in range(n2+1)] for _ in range(n1+1)]
    for j in range(n2):
        dp[0][j]=j
    for i in range(n1):
        dp[i][0]=i
    for i in range(1,n1+1):
        for j in range(1,n2+1):
            if s1[i-1]==s2[j-1]:
                dp[i][j]=min(dp[i-1][j]+1,dp[i-1][j-1],dp[i][j-1]+1)
            else:
                dp[i][j] = min(dp[i - 1][j] + 1, dp[i - 1][j - 1]+1, dp[i][j - 1] + 1)
    return dp[-1][-1]


print(editDistance('intention','execution'))
