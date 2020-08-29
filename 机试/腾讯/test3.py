'''
小Q所在的部门有n个人，要从这n个人中选任意数量的人组成一只队伍，再在这些人中选出一名队长，求不同的方案数对1e9+7取模的结果。
如果两个方案选取的人的集合不同或者选出的队长不同，则认为这两个方案是相同的。
sum=1*C(n,1)+2*C(n,2)+....+n*C(n,n)=n*2^(n-1)
经过一顿推导可以得到最终的结果为 n*2^(n-1)
'''
def solve(n):
    cnt=0
    A=1
    for m in range(1,n//2+1):
        A=A*(n-m+1)
        cnt+=A
        A/=m
    cnt*=2
    if n&1==1:
        t=n//2+1
        A = A * (n - t+ 1)
        cnt += A
    return int(cnt)%1000000007

def solve2(n):
    return (n*2**(n-1))%1000000007
if __name__ == '__main__':
    print(solve2(10**6))