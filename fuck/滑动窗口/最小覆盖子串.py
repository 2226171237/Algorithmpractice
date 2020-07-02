'''
给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字符的最小子串。
示例：
输入: S = "ADOBECODEBANC", T = "ABC"
输出: "BANC"
说明：
如果 S 中不存这样的子串，则返回空字符串 ""。
如果 S 中存在这样的子串，我们保证它是唯一的答案。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-window-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        minLen=2**32
        needs=dict()
        windows = dict()
        for x in t:
            needs[x]=needs.get(x,0)+1
            windows[x]=0
        match=0
        need_match=len(needs)

        left=0
        right=0
        start=0
        while right<len(s):
            c=s[right]
            if c in needs:
                windows[c]=windows.get(c,0)+1
                if windows[c]==needs[c]:
                    match+=1
            # 匹配了
            while match==need_match:
                if right-left+1<minLen:
                    start=left
                    minLen=right-left+1
                c=s[left]
                if c in needs:
                    windows[c]-=1
                    if windows[c]<needs[c]:
                        match-=1
                left+=1
            right+=1
        return '' if minLen==2**32 else s[start:start+minLen]

if __name__ == '__main__':
    s=Solution()
    print(s.minWindow('ADOBECODEBANC','ABC'))