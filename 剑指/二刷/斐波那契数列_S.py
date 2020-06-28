'''
写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项。斐波那契数列的定义如下：
'''

class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=1:
            return n
        prev=0
        cur=1
        for i in range(2,n+1):
            cur,prev=cur+prev,cur
        return cur%1000000007

if __name__ == '__main__':
    s=Solution()
    print(s.fib(4))