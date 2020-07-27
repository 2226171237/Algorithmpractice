

def editDist(s1,s2):
    n1=len(s1)
    n2=len(s2)
    DP=[[0 for _ in range(n2+1)] for _ in range(n1+1)]
    for i in range(n1+1):
        DP[i][0]=i
    for i in range(n2+1):
        DP[0][i]=i
    for i in range(1,n1+1):
        for j in range(1,n2+1):
            if s1[i-1]==s2[j-1]:
                DP[i][j]=min(DP[i-1][j]+1,DP[i][j-1]+1,DP[i-1][j-1])
            else:
                DP[i][j] = min(DP[i - 1][j] + 1, DP[i][j - 1] + 1, DP[i - 1][j - 1]+1)
    return DP[-1][-1]

if __name__ == '__main__':
    print(editDist('abcd','bdf'))
