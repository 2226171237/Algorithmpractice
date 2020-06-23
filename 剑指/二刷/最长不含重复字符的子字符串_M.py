'''
请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。

示例 1:
输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

提示：
s.length <= 40000
'''
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        最后一个超时
        :type s: str
        :rtype: int
        """
        # P[i][j] 代表s_i....s_j 是不是有重复字母的子串
        N=len(s)
        if N==0:
            return 0
        P=[[False for _ in range(N)] for _ in range(N)]
        for i in range(N):
            P[i][i]=True
        maxLen=1
        for j in range(1,N):
            for i in range(j-1,-1,-1):
                if P[i][j-1]:
                    P[i][j]=s[i]!=s[j] and P[i][j-1] and P[i+1][j]
                if P[i][j]:
                    maxLen=max(maxLen,j-i+1)
        return maxLen

    def lengthOfLongestSubstring2(self, s):
        '''哈希表，滑动窗口'''
        d=dict()
        maxLen=0
        begin=-1
        for end,x in enumerate(s):
            if x in d:
                begin=max(begin,d[x])
            d[x]=end
            maxLen=max(maxLen,end-begin)
        return maxLen

if __name__ == '__main__':
    s=Solution()
    print(s.lengthOfLongestSubstring2('abcabxxcbb'))
