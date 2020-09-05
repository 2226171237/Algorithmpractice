
import sys

def solve(n):
    if n==0:
        return 1
    if n==1:
        return 1
    if n==2:
        return 2
    dp=[0 for _ in range(n+1)]
    dp[0]=1
    dp[1]=1
    dp[2]=2
    for i in range(3,n+1):
        for j in range(1,7):
            dp[i]+=dp[i-j] if i-j>=0 else 0
    return dp[-1]

if __name__ == '__main__':
    print(solve(4))