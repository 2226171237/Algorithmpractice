
'''增加最少的括号使得括号匹配，只包含[]和()'''
def solve(s):
    match = {']': '[', ')': '('}
    stack=[]
    cnt=0
    for ch in s:
        if ch in '([':
            stack.append(ch)
        else:
            if match[ch] in stack:
                while len(stack) and stack[-1]!=match[ch]:
                    cnt+=1
                    stack.pop()
            else:
                cnt+=1
    return cnt

# s=sys.stdin.readline().strip()
# print(solve(s))

if __name__ == '__main__':
    print(solve(')([]]([(](])))([]()()]([][[)[()[)]([[(])][][[[([)]'))
    print(solve('[)]([)'))