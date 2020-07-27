'''
实现函数double Power(double base, int exponent)，求base的exponent次方。不得使用库函数，同时不需要考虑大数问题。

示例 1:
输入: 2.00000, 10
输出: 1024.00000
示例 2:
输入: 2.10000, 3
输出: 9.26100
示例 3:
输入: 2.00000, -2
输出: 0.25000
解释: 2-2 = 1/22 = 1/4 = 0.25
 
说明:
-100.0 < x < 100.0
n 是 32 位有符号整数，其数值范围是 [−2^31, 2^31 − 1] 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zhi-de-zheng-shu-ci-fang-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        N=abs(n)
        result=1
        while N>0:
            t_result=x
            size = 1
            while size<N//2:
                t_result*=t_result
                size*=2
            result*=t_result
            N-=size
        if n>0:
            return result
        else:
            return 1/result

    def myPow2(self, x, n):

        if n==0:
            return 1
        if n==1:
            return x
        result=self.myPow2(x,n//2)
        result*=result
        if n%2==1:
            result*=x
        return result



if __name__ == '__main__':
    s=Solution()
    print(s.myPow(2,31),2**31,s.myPow2(2,31))
