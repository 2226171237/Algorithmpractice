''''
给定一个以字符串表示的任意嵌套的三元表达式，计算表达式的值。
你可以假定给定的表达式始终都是有效的并且只包含数字 0-9, ?, :, T 和 F (T 和 F 分别表示真和假）。

注意：
给定的字符串长度 ≤ 10000。
所包含的数字都只有一位数。
条件表达式从右至左结合（和大多数程序设计语言类似）。
条件是 T 和 F其一，即条件永远不会是数字。
表达式的结果是数字 0-9, T 或者 F。
 
示例 1：
输入： "T?2:3"
输出： "2"
解释： 如果条件为真，结果为 2；否则，结果为 3。

示例 2：
输入： "F?1:T?4:5"
输出： "4"
解释： 条件表达式自右向左结合。使用括号的话，相当于：

             "(F ? 1 : (T ? 4 : 5))"                   "(F ? 1 : (T ? 4 : 5))"
          -> "(F ? 1 : 4)"                 或者     -> "(T ? 4 : 5)"
          -> "4"                                    -> "4"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ternary-expression-parser
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''''
class Solution:
    def parseTernary(self, expression: str) -> str:
        '''
        使用堆栈
        :param expression:
        :return:
        '''
        numStack=[]
        last_ch='G'
        for ch in expression[::-1]:
            if 0<=ord(ch)-ord('0')<=9 or ((ch=='T' or ch=='F') and last_ch!='?'):
                numStack.append(ch)
            else:
                if ch=='T':
                    a=numStack.pop()
                    numStack.pop()
                    numStack.append(a)
                if ch=='F':
                    numStack.pop()
            last_ch=ch
        return numStack[0]

S=Solution()
print(S.parseTernary('T?T?F:5:3'))