

def score(txt_arr):
    stack=[]
    for x in txt_arr:
        if x.isdigit():
            stack.append(int(x))
        elif x=='+' and len(stack)>1:
            stack.append(stack[-1]+stack[-2])
        elif x=='-' and len(stack)>1:
            stack.append(abs(stack[-1]-stack[-2]))
        elif x=='T' and len(stack)>0:
            stack.append(3*stack[-1])
        elif x=='C' and len(stack)>0:
            stack.pop()
    return sum(stack) if len(stack)>0 else 0


# import sys
# txt_arr=sys.stdin.readline().strip().split(' ')

print(score('5 2 C T + -'.split(' ')))
