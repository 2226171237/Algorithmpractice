
def maxA(N):
    mem=dict()
    def dp(n,num_a,copy):
        if (n,num_a,copy) in mem:
            return mem[(n,num_a,copy)]
        if n<=0:
            return num_a
        a=dp(n-1,num_a+1,copy)  # A
        b=dp(n-1,num_a+copy,copy) # ctrl-v
        c=dp(n-2,num_a,copy=num_a) # ctrl-A+ctrl-C
        res=max(a,b,c)
        mem[(n,num_a,copy)]=res
        return res
    return dp(N,0,0)

print(maxA(7))


def maxA2(N):
    dp=[0 for _ in range(N)]
    for i in range(N):
        dp[i]=dp[i-1]+1  # A
        for j in range(2,i):  # ctrl-C
            dp[i]=max(dp[i],dp[j-2]*(i-j+1))
    return dp[-1]

print(maxA2(7))