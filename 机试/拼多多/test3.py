'''
每分饭有 颜值y和热量x, 中餐和晚餐中各选择一个饭，也可都不选，也可只选中餐或晚餐，使得颜值和不下于T的情况下获得的热量和最小
'''
import sys
data=sys.stdin.readline().strip().split(' ')
N=int(data[0])
M=int(data[1])
T=int(data[2])

class Fan:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __lt__(self, other):
        return self.y<other.y

    def __gt__(self, other):
        return self.y>other.y

lanchs=[]
nights=[]
for _ in range(N):
    data=sys.stdin.readline().strip().split(' ')
    node=Fan(int(data[0]),int(data[1]))
    lanchs.append(node)
for _ in range(M):
    data=sys.stdin.readline().strip().split(' ')
    node = Fan(int(data[0]), int(data[1]))
    nights.append(node)

def solve(lanchs,nights,T):
    if T==0:
       return 0
    lanchs=sorted(lanchs,reverse=True)
    nights=sorted(nights,reverse=True)
    minHot=2**31
    i=0
    while i<len(lanchs):
        j = 0
        if lanchs[i].y+nights[j].y<T:
            break
        a=lanchs[i]
        if a.y>=T:
            minHot = min(minHot, a.x)
        while j<len(nights):
            b=nights[j]
            if b.y>=T:
                minHot = min(minHot, b.x)
            if a.y+b.y>=T:
                minHot=min(minHot,a.x+b.x)
            else:
                break
            j+=1
        i+=1
    return -1 if minHot==2**31 else minHot


def solve2(lanchs,nights,T):
    if T==0:
        return 0
    minHot=2**31
    for a in lanchs:
        if a.y>=T:
            minHot = min(minHot, a.x)
        for b in nights:
            if a.y+b.y>=T:
                minHot=min(minHot,a.x+b.x)
            if b.y>=T:
                minHot = min(minHot, b.x)
    return -1 if minHot==2**31 else minHot

print(solve(lanchs,nights,T))
print(solve2(lanchs,nights,T))