
def supperEggOpp1(K,N):

    mem=dict()
    def dp(K,N):
        if (K,N) in mem:
            return mem[(K,N)]
        if K==1:
            return N
        if N==0:
            return 0
        res=2**32
        for i in range(1,N+1):
            res=min(res,max(dp(K,N-i),dp(K-1,i-1))+1)
        mem[(K,N)]=res
        return res
    return dp(K,N)

def supperEggOpp2(K,N):

    mem=dict()
    def dp(K,N):
        if (K,N) in mem:
            return mem[(K,N)]
        if K==1:
            return N
        if N==0:
            return 0
        res=2**32
        lo=1
        hi=N
        while lo<=hi:
            mid=(lo+hi)//2
            no_breaks=dp(K,N-mid)
            breaks=dp(K-1,mid-1)
            if breaks>no_breaks:
                hi=mid-1
                res=min(res,breaks+1)
            else:
                lo=mid+1
                res=min(res,no_breaks+1)
        mem[(K,N)]=res
        return res
    return dp(K,N)

print(supperEggOpp1(2,9))
print(supperEggOpp2(2,9))

