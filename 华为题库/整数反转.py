"""
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:
输入: 123
输出: 321

 示例 2:
输入: -123
输出: -321

示例 3:
输入: 120
输出: 21

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-integer
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def reverse(self, x: int) -> int:
        res=[]
        sign=-1 if x<0 else 1
        n=x*sign
        while n:
            res.append(n%10)
            n=n//10
        n=0
        for x in res:
            n*=10
            n+=x
        n*=sign
        if n>=-2**31 and n<=2**31-1:  # 32位
            return n
        else:
            return 0

if __name__ == '__main__':
    S=Solution()
    print(S.reverse(1534236469))
