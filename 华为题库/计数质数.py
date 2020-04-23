'''
统计所有小于非负整数 n 的质数的数量。

示例:
输入: 10
输出: 4
解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
'''
class Solution:
    def isZhi(self,num):
        for x in range(2,int(num**0.5)+1):
            if num%x==0:
                return False
        return True
    def countPrimes(self, n: int) -> int:
        '''
        暴力，超时
        :param n:
        :return:
        '''
        if n==2:
            return 0
        cnt = 1
        for x in range(3,n,2):
            if self.isZhi(x):
                cnt+=1
        return cnt

    def countPrimes2(self, n: int) -> int:
        '''
        厄拉多塞筛选
        :param n:
        :return:
        '''
        isPrime=[True for _ in range(n)]
        cout=0
        for i in range(2,n):
            if isPrime[i]:
                cout+=1
                j=i*i
                while j<n:
                    isPrime[j]=False
                    j+=i
        return cout

if __name__ == '__main__':
    S=Solution()
    print(S.countPrimes(1500000))
    print(S.countPrimes2(1500000))