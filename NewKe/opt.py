# -*- coding:utf-8 -*-
'''
10以内的四则运算表达式。
包含括号。
方法：先将中缀表达式转化为后缀表达式，然后使用后缀表达式计算结果。
'''
class Stack:
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return len(self.items)==0

    def push(self,x):
        self.items.append(x)

    def pop(self):
        self.items.pop()

    def peek(self):
        return self.items[-1]

def inOrder2postOrder(inOrder):
    postOrder=''
    optStack=Stack()
    optPrior={'(':0,'+':1,'-':1,'*':2,'/':2} # 运算符优先级
    optchars=set('(+-*/)')
    for ch in inOrder:
        if ch not in optchars:
            postOrder+=ch
        elif optStack.isEmpty() or ch=='(':
            optStack.push(ch)
        else:
            if ch==')':
                top=optStack.peek()
                while top!='(':
                    postOrder+=top
                    optStack.pop()
                    if optStack.isEmpty():
                        raise ValueError("not match '(' and ')'! ")
                    top=optStack.peek()
                optStack.pop()
            else:
                top=optStack.peek()
                while optPrior[top]>=optPrior[ch]:
                    postOrder+=top
                    optStack.pop()
                    if optStack.isEmpty():
                        break
                    top=optStack.peek()
                optStack.push(ch)

    while not optStack.isEmpty():
        top=optStack.peek()
        postOrder+=top
        optStack.pop()
    return postOrder

def jisuan(postOrder):
    # 根据后缀表达式，计算结果
    S=Stack()
    optchars = '(+-*/)'
    for ch in postOrder:
        if S.isEmpty() or ch not in optchars:
            S.push(float(ch))
        else:
            a=S.peek()
            S.pop()
            b=S.peek()
            S.pop()
            if '+'==ch:
                S.push(a+b)
            elif '-'==ch:
                S.push(b-a)
            elif '*'==ch:
                S.push(a*b)
            elif '/'==ch:
                S.push(b/a)
    return S.peek()


# 10以内的加减乘除运算。
postOrder=inOrder2postOrder("(3-5)*(6+7*4)/3")
print(postOrder)
print(jisuan(postOrder))
