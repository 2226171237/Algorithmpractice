'''
给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字母的最小子串。

示例：
输入: S = "ADOBECODEBANC", T = "ABC"
输出: "BANC"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-window-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        双指针，滑动窗口
        :param s:
        :param t:
        :return:
        '''
        needs=Counter(t)
        need_matchs=len(needs)
        match=0 # 有多字符符合要求了

        window={}
        left,right=0,0
        start=0
        minLens=2**32
        while right<len(s):
            ch=s[right]
            if needs[ch]: # 需要匹配
                window[ch]=window.get(ch,0)+1
                if window[ch]==needs[ch]: # 该字符匹配成功
                    match+=1
            right+=1

            while match==need_matchs: # 所有都匹配成功，左边不断右移，直到不匹配
                if right-left<minLens: # 更新最小子串
                    start=left
                    minLens=right-left
                ch=s[left]
                if needs[ch]:
                    window[ch]-=1
                    if window[ch]<needs[ch]: # 出现了不匹配
                        match-=1
                left+=1
        return '' if minLens==2**32 else s[start:start+minLens]

if __name__ == '__main__':
    S=Solution()
    print(S.minWindow("cabwefgewcwaefgcf","cae"))


