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
'''
动态规划
P(i,j) 表示 Si...Sj 是否是回文子串
P(i,j) = Si==Sj and P(i+1,j-1)
'''
class Solution:
    def __init__(self):
        self.lens=0
        self.startindex=0

    def longestPalindrome1(self, s: str) -> str:
        P=[[False for _ in range(len(s))] for _ in range(len(s))]
        i=0
        # 第一个对角线初始化
        while i<len(s):
            P[i][i]=True
            i+=1
        maxs=1
        begin=0
        end=0
        # 右上方的第二个对角线初始化
        i=0
        while i<len(s)-1:
            if s[i+1]==s[i]:
                P[i][i+1]=True
                maxs=2
                begin=i
                end=i+1
            i+=1
        # 右上方的其余对角线
        for k in range(2,len(s)):
            i=0
            j=k
            while i<len(s) and j<len(s):
                P[i][j]=s[i]==s[j] and P[i+1][j-1]
                if P[i][j]:
                    if j-i+1>maxs:
                        begin=i
                        end=j
                i+=1
                j+=1
        return s[begin:end+1]

    # 中心扩展法，已字符串中心向两边扩展，找最长回文
    def expandBothSide(self,s,i,j):
        while i>=0 and j<len(s) and s[i]==s[j]:
            i-=1
            j+=1
        # i多减1了，j多加1了。
        if j-i-1>self.lens:
            self.lens=j-i-1
            self.startindex=i+1

    def longestPalindrome2(self, s: str) -> str:
        if None==s or len(s)<1:
            return None
        i=0
        while i<len(s)-1:
            self.expandBothSide(s,i,i)
            self.expandBothSide(s,i,i+1)
            i+=1
        return s[self.startindex:self.startindex+self.lens]

if __name__ == '__main__':
    S=Solution()
    print(S.longestPalindrome1('cbbd'))
    print(S.longestPalindrome2('cbbd'))