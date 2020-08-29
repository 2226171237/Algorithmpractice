

import sys

def solve(n,a,b):
    maxScore=[0]
    st=set(range(n))
    def dfs(st,score):
        if len(st)==0:
            maxScore[0]=max(maxScore[0],score)
            return
        st_tmp=st.copy()
        for i in st_tmp:
            st.remove(i)
            t=score*2 if b[i]==1 else 0
            t=max(t,score+a[i])
            dfs(st,t)
            st.add(i)
    dfs(st,0)
    return maxScore[0]

def solve2(n,a,b):
    st = set(range(n))
    mem=dict()
    def dfs(st,score):
        if (frozenset(st),score) in mem:
            return mem[(frozenset(st),score)]
        if len(st) == 0:
            return score
        st_tmp = st.copy()
        maxScore=0
        for i in st_tmp:
            st.remove(i)
            t = score * 2 if b[i] == 1 else 0
            t = max(t, score + a[i])
            maxScore=max(dfs(st, t),maxScore)
            st.add(i)
        mem[(frozenset(st), score)]=maxScore
        return maxScore
    return dfs(st,0)

def solve3(n,a,b):
    '''贪心'''
    score=0
    other=[]
    for i in range(n):
        if b[i]==0:
            score+=a[i]
        else:
            other.append(a[i])
    other=sorted(other,reverse=True)
    for x in other:
        score=max(score*2,score+x)
    return score

# n=int(sys.stdin.readline().strip())
# a=[]
# b=[]
# s=sys.stdin.readline().strip()
# while len(s):
#     s=s.split(' ')
#     a.append(int(s[0]))
#     b.append(int(s[1]))
#     s = sys.stdin.readline().strip()
# print(solve(n,a,b))

if __name__ == '__main__':
    print(solve2(5,[1,3,5,2,2],[1,1,1,0,0]))
    print(solve3(5, [1, 3, 5, 2, 2], [1, 1, 1, 0, 0]))