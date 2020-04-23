'''
给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。

注意：
num1 和num2 的长度都小于 5100.
num1 和num2 都只包含数字 0-9.
num1 和num2 都不包含任何前导零。
你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-strings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1)==0:
            return num2
        if len(num2)==0:
            return num1
        num1=list(num1)[::-1]
        num2=list(num2)[::-1]
        S,C=0,0
        result=[]
        i=0
        while i<len(num1) and i<len(num2):
            S=ord(num1[i])+ord(num2[i])-2*ord('0')+C
            S,C=S%10,S//10
            result.append(str(S))
            i+=1
        num =num1 if i<len(num1) else num2
        while i<len(num):
            S=ord(num[i])-ord('0')+C
            S, C = S % 10, S // 10
            result.append(str(S))
            i+=1
        if C:
            result.append('1')
        return ''.join(result[::-1])

if __name__ == '__main__':
    S=Solution()
    print(S.addStrings('99999','4567'))
