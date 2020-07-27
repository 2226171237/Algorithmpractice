'''
移掉K位数字
给定一个以字符串表示的非负整数 num，移除这个数中的 k 位数字，使得剩下的数字最小。
'''
import sys
string=sys.stdin.readline().strip()
k=int(sys.stdin.readline().strip())

def getResult(string:str,k:int):
    Stack=[]
    for ch in string:
        while k and Stack and Stack[-1]>ch:
            Stack.pop()
            k-=1
        Stack.append(ch)
    result=Stack[:-k] if k else Stack
    return ''.join(result)


if __name__ == '__main__':
    getResult()