
# 栈
def isValid(s):
    stack=[]
    s_map={')':'(','}':'{',']':"["}
    for ch in s:
        if len(stack)==0 or ch in '({[':
            stack.append(ch)
        else:
            if len(stack) and s_map[ch]==stack[-1]:
                stack.pop()
            else:
                return False
    return True if len(stack)==0 else False

