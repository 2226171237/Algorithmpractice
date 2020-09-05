

def math_op(a,b,op):
    if op=='+':
        return a+b
    elif op=='-':
        return a-b
    elif op=='*':
        return a*b
    elif op=='/':
        return a/b


def split_exp(strs):
    data = []
    i = 0
    while i < len(strs):
        c = strs[i]
        if c in '()+-*/':
            data.append(c)
            i += 1
        elif c == ' ':
            while i < len(strs) and strs[i] == ' ':
                i += 1
        else:
            num = 0
            while i < len(strs) and strs[i].isdigit():
                num = num * 10 + (ord(strs[i]) - ord('0'))
                i += 1
            data.append(num)
    return data

def calculate(strs:str):
    # 先处理数据,将操作符，数据分开
    data=split_exp(strs)
    # 计算
    opt_stack=[]  # 操作符堆栈
    data_stack=[] # 变量堆栈
    prior_op={'(':0,'+':1,'-':1,'*':2,'/':2} # 优先级
    for x in data:
        if not isinstance(x,str):
            data_stack.append(x)
        else:
            if len(opt_stack)==0 or x=='(':
                opt_stack.append(x)
            elif x==')':
                while opt_stack[-1]!='(':
                    a=data_stack.pop()
                    b=data_stack.pop()
                    op=opt_stack.pop()
                    data_stack.append(math_op(b,a,op))
                opt_stack.pop()
            elif prior_op[x]<=prior_op[opt_stack[-1]]:
                a=data_stack.pop()
                b=data_stack.pop()
                op=opt_stack.pop()
                data_stack.append(math_op(b,a,op))
                opt_stack.append(x)
            else:
                opt_stack.append(x)

    while len(opt_stack):
        a=data_stack.pop()
        b=data_stack.pop()
        op=opt_stack.pop()
        data_stack.append(math_op(b,a,op))
    return data_stack[0]


if __name__ == '__main__':
    print(calculate("( 1+ ( 4+5*12)  -3) +16/8 "))


