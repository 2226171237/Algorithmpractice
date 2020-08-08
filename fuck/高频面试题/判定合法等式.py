

class UnionFind1:
    def __init__(self,N):
        self.ids=[i for i in range(N)]
        self._count=N

    def count(self):
        return self._count

    def find(self,p):
        return self.ids[p]

    def union(self,p,q):
        p_id=self.find(p)
        q_id=self.find(q)
        if p_id==q_id:
            return
        for i in range(len(self.ids)):
            if self.ids[i]==p_id:
                self.ids[i]=q_id
        self._count-=1

    def connected(self,p,q):
        p_id=self.find(p)
        q_id=self.find(q)
        return p_id==q_id

class UnionFind:
    def __init__(self,N):
        self.ids=[i for i in range(N)]
        self._count=N

    def count(self):
        return self._count

    def find(self,p):
        while p!=self.ids[p]:
            p=self.ids[p]
        return p

    def union(self,p,q):
        p_id=self.find(p)
        q_id=self.find(q)
        if p_id==q_id:
            return
        self.ids[p_id]=q_id
        self._count-=1

    def connected(self,p,q):
        p_id=self.find(p)
        q_id=self.find(q)
        return p_id==q_id

def solve(equations):
    UF=UnionFind(26)
    for s in equations:
        x=s[0]
        op=s[1:3]
        y=s[-1]
        if op=='==':
            UF.union(ord(x)-ord('a'),ord(y)-ord('a'))
    for s in equations:
        x=s[0]
        op=s[1:3]
        y=s[-1]
        if op=='!=':
            if UF.connected(ord(x)-ord('a'),ord(y)-ord('a')):
                return False
    return True


print(solve(['a==b','b==c','c==d','b==d']))