
class UnionFind1:
    '''quick-find实现'''
    def __init__(self,N):
        '''N个触点'''
        self._ids=[i for i in range(N)] # 初始化，每个触点各占一个连通分量
        self._counts=N

    def union(self,p,q):
        '''在p和q之间添加一条连接'''
        pID=self.find(p)
        qID=self.find(q)
        if pID==qID:
            return
        # 如果不在一个连通分量力，则将其合并，q的连通号改为p的连通号
        for i in range(len(self._ids)):
            if self._ids[i]==qID:
                self._ids[i]=pID
        self._counts-=1

    def find(self,p):
        '''p所在分量的标识符'''
        return self._ids[p]

    def connected(self,p,q):
        '''p，q是否存在于同一分量'''
        return self._ids[p]==self._ids[q]

    def count(self):
        '''连通分量的数目'''
        return self._counts

class UnionFind2:
    '''quick-union实现'''
    def __init__(self,N):
        '''N个触点'''
        self._ids=[i for i in range(N)] # 初始化，每个触点各占一个连通分量
        self._counts=N

    def union(self,p,q):
        '''在p和q之间添加一条连接'''
        pRoot=self.find(p)
        qRoot=self.find(q)
        if pRoot==qRoot:
            return
        # 如果不在一个连通分量力，则将其合并
        self._ids[qRoot]=pRoot
        self._counts-=1

    def find(self,p):
        '''p所在分量的标识符'''
        while self._ids[p]!=p:
            p=self._ids[p]
        return p

    def connected(self,p,q):
        '''p，q是否存在于同一分量'''
        pRoot = self.find(p)
        qRoot = self.find(q)
        return pRoot == qRoot

    def count(self):
        '''连通分量的数目'''
        return self._counts

class UnionFind3:
    '''加权的quick-union实现'''
    def __init__(self,N):
        '''N个触点'''
        self._ids=[i for i in range(N)] # 初始化，每个触点各占一个连通分量
        self._size=[1 for _ in range(N)] # 每棵树的大小
        self._counts=N

    def union(self,p,q):
        '''在p和q之间添加一条连接'''
        pRoot=self.find(p)
        qRoot=self.find(q)
        if pRoot==qRoot:
            return
        # 如果不在一个连通分量力，将小树连到大树上，则将其合并
        if self._size[qRoot]>self._size[pRoot]:
            self._ids[pRoot]=qRoot
            self._size[qRoot]+=self._size[pRoot]
        else:
            self._ids[qRoot] = pRoot
            self._size[pRoot] += self._size[qRoot]
        self._counts-=1

    def find(self,p):
        '''p所在分量的标识符'''
        while self._ids[p]!=p:
            p=self._ids[p]
        return p

    def connected(self,p,q):
        '''p，q是否存在于同一分量'''
        pRoot = self.find(p)
        qRoot = self.find(q)
        return pRoot == qRoot

    def count(self):
        '''连通分量的数目'''
        return self._counts