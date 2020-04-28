'''
给定一个整数，将其转化为7进制，并以字符串形式输出。

示例 1:
输入: 100
输出: "202"

示例 2:
输入: -7
输出: "-10"
'''

class Solution:
    def convertToBase7(self, num: int) -> str:
        sign=-1 if num<0 else 1
        num=abs(num)
        result=[]
        while num>=7:
            result.append(str(num%7))
            num=num//7
        if num>0:
            result.append(str(num))
        if sign<0:
            return '-'+''.join(result[::-1])
        else:
            return ''.join(result[::-1])

if __name__ == '__main__':
    S=Solution()
    print(S.convertToBase7(120))