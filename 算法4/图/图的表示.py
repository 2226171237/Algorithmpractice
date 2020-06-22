
class Graph:
    def __init__(self,V):
        self._V=V
        self._E=0
        self.verterx=[[] for _ in range(V)] # 邻接表表示

    def V(self):
        '''图的顶点数'''
        return self._V

    def E(self):
        ''' 图的边数'''
        return self._E

    def adj(self,v):
        '''顶点v的相邻顶点'''
        return self.verterx[v]

    def addEdge(self,v,w):
        '''添加边'''
        self.verterx[v].append(w)
        self.verterx[w].append(v)
        self._E+=1

    def degree(self,v):
        '''计算顶点v的度'''
        degree=0
        for _ in self.adj(v):
            degree+=1
        return degree

    def maxDegree(self):
        '''图的最大度'''
        maxd=0
        for v in range(self.V()):
            maxd=max(maxd,self.degree(v))
        return maxd

    def avgDegree(self):
        '''图的平均度数'''
        return 2*self.E()/self.V()

    def numberOfSelfLoops(self):
        '''自环的数目'''
        cnt=0
        for v in range(self.V()):
            for w in self.adj(v):
                if w==v:
                    cnt+=1
        return cnt//2 # 每条边被记录了两次

    def __str__(self):
        S='verterx number: %d, edge numbers: %d\n' % (self.V(),self.E())
        for v in range(self.V()):
            t=str(v)+': '
            for w in self.adj(v):
                t+=str(w)+' '
            t+='\n'
            S+=t
        return S

class Search:
    '''图处理算法，找到起点s连通的所有顶点'''
    def __init__(self,G:Graph,s):
        self._connects=[]
        self.V=G.V()
        self.visited=[False for _ in range(G.V())]
        self.dfs(G,s,self.visited)

    def dfs(self,G:Graph,s,visited):
        if visited[s]:
            return
        visited[s]=True
        self._connects.append(s)
        for v in G.adj(s):
            if not visited[v]:
                self.dfs(G,v,visited)

    def marked(self,v):
        '''起点s是否和v连通'''
        return self.visited[v]

    def count(self):
        '''起点s锁连通的顶点数'''
        return len(self._connects)

    def isConnected(self):
        return self.count()==self.V

class DFSPaths:
    '''寻找单点路径'''
    def __init__(self,G:Graph,s):
        self.s=s
        self.visted=[False for _ in range(G.V())]
        self.path=[None for _ in range(G.V())]
        self.dfs(G,s)

    def hasPathTo(self,v):
        '''是否存在从s到v的路径'''
        return self.visted[v]

    def dfs(self,G:Graph,s):
        self.visted[s]=True
        for w in G.adj(s):
            if not self.visted[w]:
                self.path[w]=s
                self.dfs(G,w)

    def pathTo(self,v):
        '''s到v的路径，如果不存在返回None'''
        if not self.hasPathTo(v):
            return None
        path=[v]
        while self.path[v] and self.path[v]!=self.s:
            v=self.path[v]
            path.append(v)
        path.append(self.s)
        return path[::-1]


from collections import deque
class BFSPaths:
    '''寻找单点最短路径'''
    def __init__(self,G:Graph,s):
        self.s=s
        self.visted=[False for _ in range(G.V())]
        self.path=[None for _ in range(G.V())]
        self.bfs(G,s)

    def hasPathTo(self,v):
        '''是否存在从s到v的路径'''
        return self.visted[v]

    def bfs(self,G:Graph,s):
        Q=deque()
        Q.append(s)
        self.visted[s] = True
        while len(Q):
            v=Q.popleft()
            for w in G.adj(v):
                if not self.visted[w]:
                    self.visted[w] = True
                    Q.append(w)
                    self.path[w]=v

    def pathTo(self,v):
        '''s到v的路径，如果不存在返回None'''
        if not self.hasPathTo(v):
            return None
        path=[v]
        while self.path[v] and self.path[v]!=self.s:
            v=self.path[v]
            path.append(v)
        path.append(self.s)
        return path[::-1]

class CC:
    '''连通分量'''
    def __init__(self,G:Graph):
        self.ids=[None for _ in range(G.V())]
        self.visted=[False for _ in range(G.V())]
        self._count=0
        for s in range(G.V()):
            if not self.visted[s]:
                self._dfs(G,s)
                self._count+=1

    def _dfs(self,G,s):
        self.visted[s]=True
        self.ids[s]=self._count
        for v in G.adj(s):
            if not self.visted[v]:
                self._dfs(G,v)

    def connected(self,v,w):
        '''v 和 w是否连通'''
        return self.ids[v]==self.ids[w]

    def count(self):
        '''连通分量数'''
        return self._count+1

    def id(self,v):
        '''v所在的连通分量标识符 0--count()-1'''
        return self.ids[v]

class Cycle:
    '''是否有环'''
    def __init__(self,G:Graph):
        self.marked=[False for _ in range(G.V())]
        self._hasCycle=False
        for s in range(G.V()):
            if not self.marked[s]:
                self._dfs(G,s,s)

    def _dfs(self,G:Graph,u,v):
        self.marked[u]=True
        for w in G.adj(u):
            if not self.marked[w]:
                self._dfs(G,w,v)
            else:
                if w==v:
                    self._hasCycle=True

    def hasCycle(self):
        return self._hasCycle

class TwoColor:
    '''双着色问题'''
    def __init__(self,G:Graph):
        self.marked=[False for _ in range(G.V())]
        self.color=[False for _ in range(G.V())]
        self._isTwoColorable=True
        for v in range(G.V()):
            if not self.marked[v]:
                self._dfs(G,v)

    def _dfs(self,G:Graph,v):
        self.marked[v]=True
        for w in G.adj(v):
            if not self.marked[w]:
                self.color[w]=not self.color[v]
                self._dfs(G,w)
            else:
                if self.color[w]==self.color[v]:
                    self._isTwoColorable=False

    def isBipartite(self):
        return self._isTwoColorable



class SymbolGraph(Graph):
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
        super(SymbolGraph,self).__init__(idx)
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

    def __str__(self):
        S='vertex number: %d, edge numbers: %d\n' % (self.V(),self.E())
        for v in range(self.V()):
            t=self.idx2key[v]+': '
            for w in self.adj(v):
                t+=self.idx2key[w]+' '
            t+='\n'
            S+=t
        return S

class DegreesOfSeparation:
    def __init__(self,G:SymbolGraph,source):
        self.g=G
        self.bfs=BFSPaths(G,G.index(source))

    def path(self,v):
        rpath=[]
        if self.g.contain(v):
            if self.bfs.hasPathTo(self.g.index(v)):
                for p in self.bfs.pathTo(self.g.index(v)):
                    rpath.append(self.g.name(p))
        return rpath

if __name__ == '__main__':
    v=6
    E=[(0,1),(0,2),(0,4),(2,4),(3,5)]
    G=Graph(v)
    for v, w in E:
        G.addEdge(v,w)
    print(G)
    search=Search(G,0)
    print(search.isConnected())
    print(G.avgDegree())
    p=DFSPaths(G,0)
    for w in range(5):
        print(p.pathTo(w))

    p = BFSPaths(G, 0)
    for w in range(5):
        print(p.pathTo(w))

    c = CC(G)
    print(c.ids)

    sygraph=SymbolGraph('movies.txt',',')
    print(sygraph)
    twocolor=TwoColor(sygraph)
    print(twocolor.isBipartite())
    cycle=Cycle(sygraph)
    print(cycle.hasCycle())
    ds=DegreesOfSeparation(sygraph,'LAX')
    print(ds.path("JFK"))
