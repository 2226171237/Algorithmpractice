'''
实现 pow(x, n) ，即计算 x 的 n 次幂函数。

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
链接：https://leetcode-cn.com/problems/powx-n
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        sign=-1 if n<0 else 1
        n=abs(n)
        res=1
        res_t=n
        while res_t:
            t=1
            t_res=x
            while t*2<res_t:
                t_res*=t_res
                t*=2
            res_t-=t
            res*=t_res
        return res if sign==1 else 1/res

if __name__ == '__main__':
    s=Solution()
    print(s.myPow(2,-4))
