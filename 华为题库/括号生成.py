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

class Solution:
    def generateParenthesis(self, n: int):
        '''
        回溯，递归
        :param n:
        :return:
        '''
        result=[]
        def getresult(leftnum,righnum,path):
            if leftnum==righnum==n:
                result.append(''.join(path))
                return
            if leftnum>n or righnum>n:
                return
            if leftnum>righnum:
                path.append('(')
                getresult(leftnum+1,righnum,path)
                path.pop()
                path.append(')')
                getresult(leftnum, righnum+1, path)
                path.pop()
            elif leftnum<=righnum:
                path.append('(')
                getresult(leftnum+1,righnum,path)
                path.pop()

        getresult(0,0,[])
        return result

if __name__ == '__main__':
    S=Solution()
    print(S.generateParenthesis(3))