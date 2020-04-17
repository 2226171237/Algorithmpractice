'''
给定一个经过编码的字符串，返回它解码后的字符串。
编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。
你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。
此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。

示例:
s = "3[a]2[bc]", 返回 "aaabcbc".
s = "3[a2[c]]", 返回 "accaccacc".
s = "2[abc]3[cd]ef", 返回 "abcabccdcdcdef".

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/decode-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def decodeString(self, s: str) -> str:
        if len(s)==0:
            return ''
        Stack=[]
        Times=0
        for ch in s:
            if ch==']':
                subS=[]
                while Stack[-1]!='[':
                    subS.append(Stack.pop())
                Stack.pop()
                num=Stack.pop()
                Stack.append(''.join(subS[::-1])*num)
            elif ch =='[':
                Stack.append(Times)
                Times=0
                Stack.append(ch)
            elif '0'<=ch<='9':
                Times=Times*10+ord(ch)-ord('0')
            else:
                Stack.append(ch)

        return ''.join(Stack)

if __name__ == '__main__':
    S=Solution()
    print(S.decodeString("3[a]2[bc]"))
    print(S.decodeString("3[a2[c]]"))
    print(S.decodeString("2[abc]3[cd]ef"))
    print(S.decodeString("2[a1[2[r]we]efr]xr"))

