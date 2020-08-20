'''
给定两个字符串 text1 和 text2，返回这两个字符串的最长公共子序列的长度。
一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。两个字符串的「公共子序列」是这两个字符串所共同拥有的子序列。
若这两个字符串没有公共子序列，则返回 0。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-common-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        str1Len=len(text1)
        str2Len=len(text2)
        DP=[[0 for _ in range(str2Len+1)] for _ in range(str1Len+1)]
        for i in range(1,str1Len+1):
            for j in range(1,str2Len+1):
                if text1[i-1]==text2[j-1]:
                    DP[i][j]=max(DP[i-1][j-1]+1,DP[i][j-1],DP[i-1][j])
                else:
                    DP[i][j]=max(DP[i][j-1],DP[i-1][j])
        return DP[-1][-1]

if __name__ == '__main__':
    s=Solution()
    print(s.longestCommonSubsequence('abcde','ace'))