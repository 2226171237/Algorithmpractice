'''
数字以0123456789101112131415…的格式序列化到一个字符序列中。
在这个序列中，第5位（从下标0开始计数）是5，第13位是1，第19位是4，等等。

请写一个函数，求任意第n位对应的数字。

示例 1：
输入：n = 3
输出：3
示例 2：
输入：n = 11
输出：0
 
限制：
0 <= n < 2^31

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zi-xu-lie-zhong-mou-yi-wei-de-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<10:
            return n
        layer=1
        num=10
        while True:
            if n-num*layer<0:
                break
            n-=num*layer
            layer += 1
            num *= 10
        t=10**(layer-1)+n//layer
        n%=layer
        return str(t)[n]


if __name__ == '__main__':
    s=Solution()
    print(s.findNthDigit(1000))