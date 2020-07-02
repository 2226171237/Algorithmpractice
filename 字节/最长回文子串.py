'''
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：
输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：
输入: "cbbd"
输出: "bb"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindromic-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        N=len(s)
        if N==0:
            return ""
        P=[[False for _ in range(N)] for _ in range(N)]

        maxLen=1
        start=0
        for i in range(N):
            if i+1<N and s[i]==s[i+1]:
                P[i][i+1]=True
                start=i
                maxLen=2
            P[i][i]=True

        i=0
        j=2
        while j<N:
            ii,jj=i,j
            while ii<N and jj<N:
                P[ii][jj]=P[ii+1][jj-1] and s[ii]==s[jj]
                if P[ii][jj]:
                    if maxLen<jj-ii+1:
                        start=ii
                        maxLen=jj-ii+1
                ii+=1
                jj+=1
            j+=1
        return s[start:start+maxLen]

    def longestPalindrome2(self, s):
        '''中心扩展法'''

        def scanf(s,low,high):
            n=len(s)
            i=low
            j=high
            while i>=0 and j<n:
                if s[i]==s[j]:
                    i-=1
                    j+=1
                else:
                    break
            return s[i+1:j]

        subStr=''
        for i in range(len(s)):
            subA=scanf(s,i,i)
            subB=scanf(s,i,i+1)
            sub=subA if len(subA)>len(subB) else subB
            if len(sub)>len(subStr):
                subStr=sub
        return subStr
    
if __name__ == '__main__':
    s=Solution()
    print(s.longestPalindrome('aabcacb'))


