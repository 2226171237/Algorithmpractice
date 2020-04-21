'''
实现一个基本的计算器来计算一个简单的字符串表达式的值。
字符串表达式可以包含左括号 ( ，右括号 )，加号 + ，减号 -，非负整数和空格  。

示例 1:
输入: "1 + 1"
输出: 2

示例 2:
输入: " 2-1 + 2 "
输出: 3

示例 3:
输入: "(1+(4+5+2)-3)+(6+8)"
输出: 23
说明：

你可以假设所给定的表达式都是有效的。
请不要使用内置的库函数 eval。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/basic-calculator
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

def math(a,b,opt):
    if opt=='+':
        return a+b
    elif opt=='-':
        return a-b
    elif opt=='*':
        return a*b
    elif opt=='/':
        return a/b

class Solution:

    def inorder2afterOrder(self,s):
        '''
        中缀表达式，到后缀表达式
        :param s:
        :return:
        '''

    def calculate(self, s: str) -> int:
        '''
        直接用中缀表达式计算。
        当运算符优先级大时则直接入栈，当小于等于时则出栈计算。
        :param s:
        :return:
        '''
        prior={'(':0,'-':1,'+':1,'*':2,'/':2} # 运算优先级
        optchars='(+-*/)'
        VariableStack=[]
        OptStack=[]
        num=0
        i=0
        isCal=False  # 是否有数字被计算
        while i<len(s):
            # 去掉空格
            if s[i]==' ':
                i+=1
                continue
            if s[i] not in optchars:
                num=num*10+ord(s[i])-ord('0')
                isCal=True
            else:
                if isCal:
                    VariableStack.append(num)
                    num = 0
                    isCal=False
                if len(OptStack)==0 or s[i]=='(': # 空栈或左括号直接入栈
                    OptStack.append(s[i])
                elif s[i]==')': # 计算，直到出现左括号
                    while OptStack[-1]!='(':
                        a = VariableStack.pop()
                        b = VariableStack.pop()
                        VariableStack.append(math(b, a, OptStack.pop()))
                    OptStack.pop() # '('弹出
                elif prior[s[i]]>prior[OptStack[-1]]: # 优先级大直接入栈
                    OptStack.append(s[i])
                else: # 优先级相等或小于则计算
                    a=VariableStack.pop()
                    b=VariableStack.pop()
                    VariableStack.append(math(b,a,OptStack.pop()))
                    OptStack.append(s[i])
            i+=1

        # 最后还有一个没有入栈
        if isCal:
            VariableStack.append(num)

        # 计算其余
        while len(OptStack):
            a = VariableStack.pop()
            b = VariableStack.pop()
            VariableStack.append(math(b, a, OptStack.pop()))
        return VariableStack[-1]


if __name__ == '__main__':
    S=Solution()
    print(S.calculate("(3-5)*(6+7*4)/3"))

