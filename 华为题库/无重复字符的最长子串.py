""""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:
输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""""
class Solution:
    def lengthOfLongestSubstring1(self, s: str) -> int:
        '''
        动态规划，P(i,j) 表示si...sj子串是不是非重复的子串
        当si==sj 时，P(i,j)=0
        当si！=sj 时，P(i,j)=P(i,j-1) and P(i+1,j)
        超出时间限制了
        :param s:
        :return:
        '''
        if None==s or len(s)<1:
            return 0

        maxLens=1
        P=[[False for _ in range(len(s))] for _ in range(len(s)) ]
        # 初始化主对角线
        i=0
        while i<len(s):
            P[i][i]=True
            i+=1

        for k in range(1,len(s)):
            i=0
            j=k
            while i<len(s) and j<len(s):
                if s[i]!=s[j]:
                    P[i][j]=P[i][j-1] and P[i+1][j]
                    if P[i][j]:
                        maxLens=maxLens if maxLens>j-i+1 else j-i+1
                else:
                    P[i][j]=False
                i+=1
                j+=1
        return maxLens

    def lengthOfLongestSubstring2(self, s: str) -> int:
        # 滑动窗口 hashmap
        hashmap=dict()
        begin,end=0,0
        maxLens=0
        while end<len(s):
            if s[end] not in hashmap:
                hashmap[s[end]]=end
            if s[end] in hashmap and hashmap[s[end]]>=begin:
                maxLens = max(maxLens,end-begin)
                begin=hashmap[s[end]]+1
            end+=1
        return maxLens

if __name__ == '__main__':
    S=Solution()
    print(S.lengthOfLongestSubstring1('pwwkew'))
    print(S.lengthOfLongestSubstring2('pwwkew'))


