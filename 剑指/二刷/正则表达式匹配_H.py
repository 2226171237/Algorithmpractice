'''
请实现一个函数用来匹配包含'. '和'*'的正则表达式。模式中的字符'.'表示任意一个字符，
而'*'表示它前面的字符可以出现任意次（含0次）。在本题中，匹配是指字符串的所有字符匹配整个模式。
例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但与"aa.a"和"ab*a"均不匹配。

示例 1:
输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
示例 2:

输入:
s = "aa"
p = "a*"
输出: true
解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。

s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母以及字符 . 和 *，无连续的 '*'。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zheng-ze-biao-da-shi-pi-pei-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class MutiSourcePath:
    def __init__(self,G,s):
        s=s if isinstance(s,(list,tuple)) else [s]
        self._marked=[False for _ in range(len(G))]
        for x in s:
            if not self._marked[x]:
                self._dfs(G,x)

    def _dfs(self,G,x):
        self._marked[x]=True
        for y in G[x]:
            if not self._marked[y]:
                self._dfs(G,y)

    def hasPathTo(self,x):
        return self._marked[x]

class NFA:
    def __init__(self,reprex):
        self.re='('+reprex+')'
        self.M=len(self.re)
        self.G=[[] for _ in range(self.M+1)]

        for i in range(self.M):
            if i<self.M-1 and self.re[i+1]=='*':
                self.G[i].append(i+1)
                self.G[i+1].append(i)
            if self.re[i] in '(*)':
                self.G[i].append(i+1)

    def isMatch(self,txt):
        pc=[]
        dfs=MutiSourcePath(self.G,0)
        for v in range(len(self.G)):
            if dfs.hasPathTo(v):
                pc.append(v)

        for i in range(len(txt)):
            match=[]
            for v in pc:
                if v<self.M:
                    if self.re[v]==txt[i] or self.re[v]=='.':
                        match.append(v+1)
            pc=[]
            dfs=MutiSourcePath(self.G,match)
            for x in range(len(self.G)):
                if dfs.hasPathTo(x):
                    pc.append(x)
        for v in pc:
            if v==self.M:
                return True
        return False

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        nfa=NFA(p)
        return nfa.isMatch(s)


if __name__ == '__main__':
    s=Solution()
    print(s.isMatch('aa','a*'))