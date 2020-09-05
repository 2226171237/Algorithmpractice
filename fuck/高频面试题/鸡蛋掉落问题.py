

mem=dict()
def dp(K,N):
    if (K,N) in mem:
        return mem[(K,N)]
    if K==1: return N
    if N==0: return 0
    res=2**31
    # for i in range(1,N+1):
    #     res=min(res,
    #             max(dp(K-1,i-1), # 碎
    #                 dp(K,N-i)   # 没碎
    #                 )+1         # 第i层仍了一次
    #             )
    # 二分查找
    lo,hi=1,N
    while lo<=hi:
        mid=(lo+hi)//2
        broken=dp(K-1,mid-1)
        no_broken=dp(K,N-mid)
        if broken>no_broken:
            hi=mid-1
            res=min(res,broken+1)
        else:
            lo=mid+1
            res=min(res,no_broken+1)
    mem[(K,N)]=res
    return res

if __name__ == '__main__':
    print(dp(100,100))