'''
如何消除字符串的内嵌括号？
给定一个如下格式的字符串：(1,(2,3),(4,(5,6),7)),括号内的元素可以是数字，也可以是另一个括号，
实现一个算法消除内嵌括号，例如把上面的表达式变成(1,2,3,4,5,6,7),如果表达式有错，则报错。
'''

class Stack:
    def __init__(self):
        self.items=[]

    def is_empty(self):
        return len(self.items)==0

    def push(self,x):
        self.items.append(x)

    def pop(self):
        if self.is_empty():
            return
        return self.items.pop()

    def top(self):
        return self.items[-1]

def removeNestedPare(s):
    st=Stack()
    st.push(s[0])
    i=1
    n=len(s)
    result='('
    while i<n:
        if s[i]=='(':
            st.push(s[i])
        elif s[i]==')':
            if not st.is_empty() and st.top()=='(':
                st.pop()
            else:
                raise  ValueError('not match')
        else:
            result+=s[i]
        i+=1
    if st.is_empty():
        result+=')'
        return result
    else:
        raise ValueError('not match')

if __name__ == '__main__':
    print(removeNestedPare('(1,(2,3),(4,5,6),7))'))