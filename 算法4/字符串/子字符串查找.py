
def search1(s,p):
    '''暴力查找'''
    N=len(s)
    M=len(p)
    for i in range(N-M):
        j=0
        while j<M and s[i+j]==p[j]:
            j+=1
        if j==M:
            return i
    return N

def search2(s,p):
    '''暴力法的另一种实现，显式回退'''

    N=len(s)
    M=len(p)
    i=0
    j=0
    while i<N and j<M:
        if s[i]==p[j]:
            j+=1
        else:
            i-=j
            j=0
        i+=1
    if j==M:
        return i-M
    else:
        return N


class BoyerMooreSearch:
    def __init__(self):
        self.R=256
        self.right=[0 for _ in range(self.R)]

    def search(self,s,p):
        N,M=len(s),len(p)
        for i in range(self.R):
            self.right[i]=-1
        for i in range(M):
            self.right[ord(p[i])]=i
        i=0
        while i<N-M:
            skip=0
            for j in range(M-1,-1,-1):
                if s[i+j]!=p[j]:
                    skip=j-self.right[ord(s[i+j])]
                    if skip<0:
                        skip=1
                    break
            if skip==0:
                return i
            i+=skip
        return N


if __name__ == '__main__':
    print(search1('hello world','worl'))
    print(search2('hello world', 'worl'))
    bm=BoyerMooreSearch()
    print(bm.search('hello world','orl'))