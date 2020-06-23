
class Edge:
    '''加权边'''
    def __init__(self,v,w,weight):
        self._v=v
        self._w=w
        self._weight=weight

    def weight(self):
        return self._weight

    def either(self):
        '''边两点的顶点之一'''
        return self._v

    def other(self,v):
        '''另一个顶点'''
        if v==self._v:
            return self._w
        elif v==self._w:
            return self._v
        else:
            raise ValueError

    def __lt__(self, other):
        '''小于'''
        return self._weight<other.weight()

    def __gt__(self, other):
        '''大于'''
        return self._weight>other.weight()

    def __eq__(self, other):
        return self._weight==other.weight()

    def __str__(self):
        s='Edge: '+str(self._v)+'--->'+ str(self._w)+ '  '+ str(self._weight)
        return s

class EdgeWeightGraph:
    '''加权无向图'''
    def __init__(self,filename=None,delim=None,V=None):
        if filename==None and V!=None:
            self._V=V
            self._E=0
            self._vertex=[[] for _ in range(V)]
        else:
            with open(filename) as f:
                self._V=int(f.readline().strip())
                self._vertex = [[] for _ in range(self._V)]
                self._E=0
                f.readline()
                for line in f.readlines():
                    line=line.strip().split(delim)
                    v=int(line[0])
                    w=int(line[1])
                    weight=float(line[2])
                    e=Edge(v,w,weight)
                    self.addEdge(e)

    def E(self):
        return self._E

    def V(self):
        return self._V

    def addEdge(self,e:Edge):
        v=e.either()
        self._vertex[v].append(e)
        self._vertex[e.other(v)].append(e)
        self._E+=1

    def adj(self,v):
        '''与v相邻的所有边'''
        return self._vertex[v]

    def edges(self):
        '''图的所有边'''
        res=[]
        for v in range(self._V):
            for e in self.adj(v):
                if e.other(v)>v:
                    res.append(e)
        return res

from queue import PriorityQueue
class LazyPrimMST:
    '''延时Prim实现最小生成树'''
    def __init__(self,G:EdgeWeightGraph):
        self._marked=[False for _ in range(G.V())] # 是否在生成树中
        self._mst=[]
        self._pq=PriorityQueue()

        self._visit(G,0)
        while not self._pq.empty():
            e=self._pq.get()  # 获取最小的边
            v=e.either()
            w=e.other(v)
            if self._marked[v] and self._marked[w]:  # 失效的边
                continue
            self._mst.append(e)
            if not self._marked[v]:
                self._visit(G,v)
            if not self._marked[w]:
                self._visit(G,w)

    def _visit(self,G,v):
        '''标记顶点并将所有连接v和未被标记顶点的边加入pq'''
        self._marked[v]=True
        for e in G.adj(v):
            if not self._marked[e.other(v)]:
                self._pq.put(e)

    def edges(self):
        '''最小生成树的所有边'''
        return self._mst

    def weight(self):
        '''最小生成树的权重和'''
        w=0
        for e in self._mst:
            w+=e.weight()
        return w


class UnionFind:
    def __init__(self,V):
        self._ids=[i for i in range(V)]
        self._count=V
        self._sz=[1 for _ in range(V)]

    def union(self,p,q):
        pRoot=self.find(p)
        qRoot=self.find(q)
        if pRoot==qRoot:
            return
        if self._sz[pRoot]>self._sz[qRoot]:
            self._ids[qRoot]=pRoot
            self._sz[pRoot]+=self._sz[pRoot]
        else:
            self._ids[pRoot]=qRoot
            self._sz[qRoot]+=self._sz[pRoot]
        self._count-=1

    def find(self,p):
        while self._ids[p]!=p:
            p=self._ids[p]
        return p

    def connected(self,p,q):
        pRoot=self.find(p)
        qRoot=self.find(q)
        return pRoot==qRoot

    def count(self):
        return self._count

class KruskalMST:
    '''Kruskal最小生成树'''
    def __init__(self,G:EdgeWeightGraph):
        self._mst=[]
        self._pq=PriorityQueue()
        self._uf=UnionFind(G.V())
        self._weights=0
        for e in G.edges():
            self._pq.put(e)
        while not self._pq.empty():
            e=self._pq.get()
            v=e.either()
            w=e.other(v)
            if self._uf.connected(v,w):
                continue
            self._uf.union(v,w)
            self._weights+=e.weight()
            self._mst.append(e)

    def edges(self):
        '''最小生成树的所有边'''
        return self._mst

    def weight(self):
        '''最小生成树的权重和'''
        return self._weights

if __name__ == '__main__':

    G=EdgeWeightGraph(filename='data/tinyEWG.txt',delim=' ')
    print(G.V())
    mst=LazyPrimMST(G)
    for e in mst.edges():
        print(e)
    print(mst.weight())
    G = EdgeWeightGraph(filename='data/1000EWG.txt', delim=' ')
    kmst=KruskalMST(G)
    print(kmst.weight())