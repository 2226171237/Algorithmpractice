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