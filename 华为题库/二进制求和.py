'''
给你两个二进制字符串，返回它们的和（用二进制表示）。
输入为 非空 字符串且只包含数字 1 和 0。

示例 1:
输入: a = "11", b = "1"
输出: "100"

示例 2:
输入: a = "1010", b = "1011"
输出: "10101"
 
提示：
每个字符串仅由字符 '0' 或 '1' 组成。
1 <= a.length, b.length <= 10^4
字符串如果不是 "0" ，就都不含前导零。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-binary
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return '{0:b}'.format(int(a,2)+int(b,2))
    def addBinary2(self, a: str, b: str) -> str:
        '''
        直接一位一位求
        :param a:
        :param b:
        :return:
        '''
        i=len(a)-1
        j=len(b)-1
        result=[]
        S,C=0,0
        while i>=0 and j>=0:
            S=ord(a[i])+ord(b[j])-2*ord('0')+C
            S,C=S%2,S//2
            result.append(str(S))
            i-=1
            j-=1
        rest,s=(i,a) if i>=0 else (j,b)
        while rest>=0:
            S=ord(s[rest])-ord('0')+C
            S, C = S % 2, S // 2
            result.append(str(S))
            rest-=1
        if C==1:
            result.append('1')
        return ''.join(result[::-1])

if __name__ == '__main__':
    S=Solution()
    print(S.addBinary('1111','1111'))
