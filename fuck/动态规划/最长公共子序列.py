

def longestCommonSubsequence(str1,str2):
    rows=len(str1)
    if rows==0:
        return 0
    cols=len(str2)
    DP=[[0 for _ in range(cols+1)] for _ in range(rows+1)]
    for i in range(1,rows+1):
        for j in range(1,cols+1):
            if str1[i-1]==str2[j-1]:
                DP[i][j]=DP[i-1][j-1]+1
            else:
                DP[i][j]=max(DP[i-1][j],DP[i][j-1])
    return DP[-1][-1]



print(longestCommonSubsequence('abcde','ace'))