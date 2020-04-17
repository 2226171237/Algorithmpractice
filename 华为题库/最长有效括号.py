'''
给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

示例 1:
输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"

示例 2:
输入: ")()())"
输出: 4
解释: 最长有效括号子串为 "()()"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-valid-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        '''
        使用堆栈，堆栈存下标
        :param s:
        :return:
        '''
        if len(s)==0:
            return 0
        Stact=[-1]
        maxLens=0
        for i,ch in enumerate(s):
            if ch=='(':
                Stact.append(i)
            else:
                Stact.pop()
                if len(Stact)==0:
                    Stact.append(i)
                else:
                    maxLens=max(maxLens,i-Stact[-1])
        return  maxLens

    def longestValidParentheses2(self, s: str) -> int:
        '''
        两遍遍历
        :param s:
        :return:
        '''
        left,right=0,0
        maxLens=0
        for x in s:
            if x=='(':
                left+=1
            else:
                right+=1
            if left==right:
                maxLens=max(maxLens,2*left)
            if right>left:
                left,right=0,0
        left,right=0,0
        for x in s[::-1]:
            if x=='(':
                left+=1
            else:
                right+=1
            if left==right:
                maxLens=max(maxLens,2*left)
            if left>right:
                right,left=0,0
        return maxLens
if __name__ == '__main__':
    S=Solution()
    print(S.longestValidParentheses(')(()(())())()()'))
    print(S.longestValidParentheses2(')(()(())())()()'))



