'''
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:
输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        windows=[0 for _ in range(256)]
        maxLen=0

        left=0
        right=0
        while right<len(s):
            c=s[right]
            windows[ord(c)]+=1
            while windows[ord(c)]>1:
                t=s[left]
                windows[ord(t)]-=1
                left+=1
            maxLen=max(right-left+1,maxLen)
            right+=1
        return maxLen

if __name__ == '__main__':
    s=Solution()
    print(s.lengthOfLongestSubstring('abcabcbb'))