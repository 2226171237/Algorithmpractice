

def maxA(N):
    mem=dict()
    def dp(n,a_num,copy):
        '''
        :param n: 剩余操作数
        :param a_num: A的数量
        :param copy: 剪切版中A的数量
        :return:
        '''
        if (n,a_num,copy) in mem:
            return mem[(n,a_num,copy)]
        if n<0:
            return 0
        if n==0:
            return a_num
        # type A:
        A=dp(n-1,a_num+1,copy)
        # type ctrl-v:
        B=dp(n-1,a_num+copy,copy)
        # type ctrl-a+ctrl-v
        C=dp(n-2,a_num,a_num)
        res=max(A,B,C)
        mem[(n, a_num, copy)]=res
        return res
    return dp(N,0,0)


def maxA2(N):
    '''
    DP(i) 表示操作第i次的A的数目，且最后一次一定是A 或ctrl-V,
    :param N:
    :return:
    '''
    DP=[0 for _ in range(N+1)]
    for i in range(1,N+1):
        DP[i]=DP[i-1]+1  # type A
        for j in range(i-3,0,-1): # type ctrl-c+ctrl-a 位置  后面连续 ctrl-v
            DP[i]=max(DP[i],DP[j]*(i-j-1))  # (i-j-2+1) 减去两个操作ctrl-c,ctrl-v ，ctrl-v的个数+1
    return DP[-1]

if __name__ == '__main__':

    print(maxA(10))
    print(maxA2(10))

