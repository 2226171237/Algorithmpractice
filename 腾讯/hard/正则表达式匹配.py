'''
给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。
说明:
s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/regular-expression-matching
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        def match(s,p):
            if len(p)==0:
                return len(s)==0
            submatch=len(s)>0 and (s[0]==p[0] or p[0]=='.')
            if len(p)>1 and p[1]=='*':
                return match(s,p[2:]) or (submatch and match(s[1:],p))
            return submatch and match(s[1:],p[1:])

        return match(s,p)

if __name__ == '__main__':
    s=Solution()
    print(s.isMatch('aa','a'))




