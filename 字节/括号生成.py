'''
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
示例：
输入：n = 3
输出：[
       "((()))",
       "(()())",
       "(())()",
       "()(())",
       "()()()"
     ]
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/generate-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        res=[]
        def find(leftp,rightp,s):
            if leftp==n and rightp==n:
                res.append(s)
                return
            if leftp>n or rightp>n:
                return
            if leftp==rightp: # 只能放左括号
                find(leftp+1,rightp,s+'(')
            elif leftp<rightp:
                return
            else: # 可放左也可放右
                find(leftp+1,rightp,s+'(')
                find(leftp,rightp+1,s+')')

        find(0,0,'')
        return res

if __name__ == '__main__':
    s=Solution()
    print(s.generateParenthesis(4))