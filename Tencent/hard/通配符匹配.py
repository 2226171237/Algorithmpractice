'''
给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。
'?' 可以匹配任何单个字符。
'*' 可以匹配任意字符串（包括空字符串）。
两个字符串完全匹配才算匹配成功。

说明:
s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/wildcard-matching
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        patten=''
        for x in p:
            if x=='*' and len(patten)>0 and patten[-1]=='*':
                continue
            patten+=x
        mem=dict()
        def match(s,p):
            if (s,p) in mem:
                return mem[(s,p)]
            if len(p)==0:
                return len(s)==0
            if len(s)==0:
                return p in '*'*len(p)
            ismatch=len(s)>0 and p[0] in [s[0],'?']
            if p[0]=='*':
                tmp=match(s[1:],p) or match(s,p[1:])
                mem[(s,p)]=tmp
                return tmp
            tmp=ismatch and match(s[1:],p[1:])
            mem[(s,p)]=tmp
            return tmp
        return match(s,patten)

    def isMatch2(self, s, p):
        '''动态规划'''
        patten = ''
        for x in p:
            if x == '*' and len(patten) > 0 and patten[-1] == '*':
                continue
            patten += x
        lenS=len(s)
        lenP=len(patten)
        dp=[[False for _ in range(lenP+1)] for _ in range(lenS+1)]
        dp[0][0]=True
        for i in range(1,lenS+1):
            dp[i][0]=False
        for j in range(1,lenP+1):
            dp[0][j]=patten[:j]=='*'
        for i in range(1,lenS+1):
            for j in range(1,lenP+1):
                if patten[j-1] in [s[i-1],'?']:
                    dp[i][j]=dp[i-1][j-1]
                elif patten[j-1]=='*':
                    dp[i][j]=dp[i-1][j] or dp[i][j-1]  # 匹配0次或多次
                else:
                    dp[i][j]=False
        return dp[-1][-1]

if __name__ == '__main__':
    s=Solution()
    print(s.isMatch("adceb",'*a*b'))
    print(s.isMatch2("adceb", '*a*b'))
