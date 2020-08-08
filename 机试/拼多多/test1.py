
import sys

data=sys.stdin.readline().strip().split(' ')
K=int(data[0])
N=int(data[1])
points=sys.stdin.readline().strip().split(' ')
points=[int(x) for x in points]

def solve(K,points):
    if K==0:
        return "paradox"
    back_time=0
    for i,x in enumerate(points):
        if x<K:
            K-=x
        else:
            K=x-K
            back_time+=1
        if K==0:
            if i<len(points)-1:
                return "paradox"
            else:
                return "%d %d" % (K, back_time)
    return "%d %d" % (K,back_time)

print(solve(K,points))

