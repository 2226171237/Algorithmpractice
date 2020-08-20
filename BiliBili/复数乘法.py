'''
给定两个表示复数的字符串。
返回表示它们乘积的字符串。注意，根据定义 i^2 = -1 。

示例 1:
输入: "1+1i", "1+1i"
输出: "0+2i"
解释: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i ，你需要将它转换为 0+2i 的形式。
示例 2:
输入: "1+-1i", "1+-1i"
输出: "0+-2i"
解释: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i ，你需要将它转换为 0+-2i 的形式。
注意:
输入字符串不包含额外的空格。
输入字符串将以 a+bi 的形式给出，其中整数 a 和 b 的范围均在 [-100, 100] 之间。输出也应当符合这种形式。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/complex-number-multiplication
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i=a.find('+')
        x1=int(a[:i])
        y1=int(a[i+1:-1])
        i = b.find('+')
        x2 = int(b[:i])
        y2 = int(b[i + 1:-1])
        x=x1*x2-y1*y2
        y=x1*y2+x2*y1
        return str(x)+'+'+str(y)+'i'

if __name__ == '__main__':
    s=Solution()
    print(s.complexNumberMultiply("1+-1i", "0+0i"))

