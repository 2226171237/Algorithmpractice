
class Digraph:
    def __init__(self,N):
        self._V=N
        self._E=0
        self.vertex=[[] for _ in range(N)]

    def V(self):
        return self._V

    def E(self):
        return self._E

    def addEdge(self,v,w):
        self.vertex[v].append(w)
        self._E+=1

    def adj(self,v):
        '''
        :param v:
        :return list[int]:
        '''
        return self.vertex[v]

    def reverse(self):
        '''反图'''
        digraph=Digraph(self._V)
        for v in range(self._V):
            for w in self.adj(v):
                digraph.addEdge(w,v)
        return digraph

    def __str__(self):
        S = 'verterx number: %d, edge numbers: %d\n' % (self.V(), self.E())
        for v in range(self.V()):
            t = str(v) + ': '
            for w in self.adj(v):
                t += str(w) + ' '
            t += '\n'
            S += t
        return S

class SymbolDigraph(Digraph):
    '''符号图'''
    def __init__(self,filename:str,delim:str):
        self.key2idx = dict()
        self.idx2key = dict()
        idx=0
        edges=[]
        with open(filename,'r') as f:
            for line in f.readlines():
                v,w=line.strip().split(delim)
                if v not in self.key2idx:
                    self.key2idx[v]=idx
                    self.idx2key[idx]=v
                    idx+=1
                if w not in self.key2idx:
                    self.key2idx[w]=idx
                    self.idx2key[idx]=w
                    idx+=1
                edges.append((self.key2idx[v],self.key2idx[w]))
        super(SymbolDigraph,self).__init__(idx)
        for v,w in edges:
            self.addEdge(v,w)

    def contain(self,key:str):
        '''key是否是一个顶点'''
        return key in self.key2idx

    def index(self,key:str):
        '''key的索引'''
        return self.key2idx[key]

    def name(self,v):
        '''索引v的顶点名'''
        return self.idx2key[v]

    def printPath(self,path):
        rpath=[]
        for p in path:
            rpath.append(self.name(p))
        return rpath
    def __str__(self):
        S='vertex number: %d, edge numbers: %d\n' % (self.V(),self.E())
        for v in range(self.V()):
            t=self.idx2key[v]+': '
            for w in self.adj(v):
                t+=self.idx2key[w]+' '
            t+='\n'
            S+=t
        return S

class DirectDFS:
    '''单点有向路径'''
    def __init__(self,G:Digraph,s):
        self.s=s
        self.marked=[False for _ in range(G.V())]
        self.paths = [False for _ in range(G.V())]
        self._dfs(G,s)

    def _dfs(self,G:Digraph,s):
        self.marked[s]=True
        for v in G.adj(s):
            if not self.marked[v]:
                self.paths[v]=s
                self._dfs(G,v)

    def hasPathTo(self,v):
        return self.marked[v]

    def pathTo(self,v):
        path=[v]
        while self.paths[v] and self.paths[v]!=self.s:
            v=self.paths[v]
            path.append(v)
        path.append(self.s)
        return path[::-1]

from collections import  deque
class DirectBFS:
    '''单点最短路径'''
    def __init__(self,G:Digraph,s):
        self.s=s
        self.marked=[False for _ in range(G.V())]
        self.paths = [False for _ in range(G.V())]
        self._bfs(G,s)

    def _bfs(self,G:Digraph,s):
        Q=deque()
        Q.append(s)
        self.marked[s]=True
        while len(Q):
            v=Q.popleft()
            for w in G.adj(v):
                if not self.marked[w]:
                    self.marked[w]=True
                    self.paths[w]=v
                    Q.append(w)

    def hasPathTo(self,v):
        return self.marked[v]

    def pathTo(self,v):
        path=[v]
        while self.paths[v] and self.paths[v]!=self.s:
            v=self.paths[v]
            path.append(v)
        path.append(self.s)
        return path[::-1]

class DirectCycle:
    '''检测是否有有向环'''
    def __init__(self,G:Digraph):
        self._hasCycle=False
        self.edgeTo=[None for _ in range(G.V())]
        self.marked=[False for _ in range(G.V())]
        self.onStack=[False for _ in range(G.V())] # 在栈中
        self._cycle=[]
        for v in range(G.V()):
            if not self.marked[v] and not self.hasCycle():
                self._dfs(G,v)

    def _dfs(self,G:Digraph,v):
        self.marked[v]=True
        self.onStack[v]=True
        if self.hasCycle():
            return
        for w in G.adj(v):
            if not self.marked[w]:
                self.edgeTo[w]=v
                self._dfs(G,w)
            else:
                if self.onStack[w]:
                    self._cycle.append(v)
                    v1 = self.edgeTo[v]
                    while v1!=w:
                        self._cycle.append(v1)
                        v1=self.edgeTo[v1]
                    self._cycle.append(w)
                    self._cycle.append(v)
                    self._hasCycle=True
                    self._cycle=self._cycle[::-1]
        self.onStack[v]=False

    def hasCycle(self):
        return self._hasCycle

    def cycle(self):
        return self._cycle


class DepthFirstOrder:
    '''深度优先搜素的顶点排序'''
    def __init__(self,G:Digraph):
        self.preOrder=[] #前序，在dfs调用前入队
        self.postOrder=[] # 后序，在dfs调用后入队
        self.reversePost=deque() # 逆后序，在dfs调用后入栈
        self.marked=[False for _ in range(G.V())]

        for v in range(G.V()):
            if not self.marked[v]:
                self._dfs(G,v)

    def _dfs(self,G:Digraph,v):
        self.marked[v]=True
        self.preOrder.append(v)
        for w in G.adj(v):
            if not self.marked[w]:
                self._dfs(G,w)
        self.postOrder.append(v)
        self.reversePost.appendleft(v)

    def pre(self):
        return self.preOrder

    def post(self):
        return self.postOrder

    def reversepost(self):
        return self.reversePost

class Topological:
    '''拓扑排序'''
    def __init__(self,G:Digraph):
        self._order=None
        cyclefilder=DirectCycle(G)
        if not cyclefilder.hasCycle():
            dfs=DepthFirstOrder(G)
            self._order=dfs.reversepost()

    def isDAG(self):
        '''是否是有向无环图'''
        return self._order==None

    def order(self):
        '''返回拓扑排序的所有顶点'''
        return self._order

class KosarajuSCC:
    '''强连通分量 Kosaraju算法'''
    def __init__(self,G:Digraph):
        re_G=G.reverse()
        dfs_order=DepthFirstOrder(re_G)
        re_order=dfs_order.reversepost() # 反图的拓扑排序
        self.marked=[False for _ in range(G.V())]
        self._ids=[i for i in range(G.V())]
        self._count=0
        for v in re_order:
            if not self.marked[v]:
                self._dfs(G,v)
                self._count+=1

    def _dfs(self,G:Digraph,v):
        self.marked[v]=True
        self._ids[v]=self._count
        for w in G.adj(v):
            if not self.marked[w]:
                self._dfs(G,w)

    def stronglyConnected(self,v,w):
        '''v，w是否是强连通的'''
        return self._ids[v]==self._ids[w]

    def count(self):
        '''强连通分量的总数'''
        return self._count

    def id(self,v):
        '''v所在的强连通分量的标识符 （0至count()-1之间）'''
        return self._ids[v]


class TransitiveClosure:
    '''传递闭包'''
    def __init__(self,G:Digraph):
        self._all=[DirectDFS(G,v) for v in range(G.V())]

    def reachable(self,v,w):
        '''v是否可达w'''
        return self._all[v].hasPathTo(w)

if __name__ == '__main__':
    G=SymbolDigraph('data/direct.txt', ',')

    # 环检测
    print('#######环检测########')
    dc=DirectCycle(G)
    print('有无环',dc.hasCycle())
    print('检测到的环',G.printPath(dc.cycle()))

    # DFS序
    print('#########DFS遍历##########')
    order=DepthFirstOrder(G)
    print('前序访问')
    print(G.printPath(order.pre()))
    print('后序访问')
    print(G.printPath(order.post()))
    print('逆后序访问')
    print(G.printPath(order.reversepost()))

    # 有向无环图的拓扑排序
    print('####有向无环图的拓扑排序####')
    tp=Topological(G)
    print(G.printPath(tp.order()))

    # 强连通分量
    print('########强连通分量#########')
    scc=KosarajuSCC(G)
    print('strongly connected compose nums',scc.count())
    compose=[[] for _ in range(scc.count())]
    for v in range(G.V()):
        i=scc.id(v)
        compose[i].append(G.name(v))
    for p in compose:
        print(p)