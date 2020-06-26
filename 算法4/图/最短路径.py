
class DirectedEdge:
    '''加权有向边'''

    def __init__(self,v,w,weight):
        self._v=v
        self._w=w
        self._weight=weight

    def come(self):
        return self._v

    def to(self):
        return self._w

    def weight(self):
        return self._weight

    def __str__(self):
        return "%d-->%d  %.2f" % (self._v,self._w,self._weight)


class EdgeWeightDigraph:
    '''加权有向图'''
    def __init__(self,filename=None,delim=None,V=None):
        if filename==None:
            self._V=V
            self._E=0
            self._vertex=[[] for _ in range(V)]
        else:
            with open(filename,'r') as f:
                self._V=int(f.readline().strip())
                self._E=int(f.readline().strip())
                self._vertex=[[] for _ in range(self._V)]
                for line in f.readlines():
                    line=line.strip().split(delim)
                    v=int(line[0])
                    w=int(line[1])
                    weight=float(line[2])
                    e=DirectedEdge(v,w,weight)
                    self.addEdge(e)

    def addEdge(self,e):
        self._vertex[e.come()].append(e)
        self._E+=1

    def adj(self,v):
        return self._vertex[v]

    def edges(self):
        res=[]
        for v in range(self._V):
            for e in self.adj(v):
                res.append(e)
        return res

    def V(self):
        return self._V

    def E(self):
        return self._E

class IndexMinPQ:
    '''索引和键关联起来的优先对立，键为优先级'''
    def __init__(self):
        self._keys=[-1]
        self._vals=[-1]
        self._d={}
        self._size=0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size==0

    def enqueue(self,key,val):
        '''入队'''
        self._keys.append(key)
        self._vals.append(val)
        self._size+=1
        self._d[key] = self._size
        self._up(self._size)

    def dequeue(self):
        '''出队'''
        if self.is_empty():
            return None
        res=self._keys[1],self._vals[1]
        self._keys[1]=self._keys[self._size]
        self._vals[1]=self._vals[self._size]
        self._keys.pop()
        self._vals.pop()
        self._d.pop(res[0])
        self._size-=1
        if not self.is_empty():
            self._down(1)
        return  res

    def change(self,key,val):
        '''改变值'''
        id=self._d[key]
        self._vals[id]=val
        v1=self._vals[id*2] if id*2<=self._size else float('inf')
        v2 = self._vals[id * 2+1] if id*2+1 <= self._size else float('inf')
        if val<min(v1,v2):
            self._up(id)
        else:
            self._down(id)

    def contain(self,key):
        return key in self._d

    def _up(self,current):
        current_idx=current
        parent_idx=self._size//2
        while current_idx>1:
            if self._vals[current_idx]<self._vals[parent_idx]:
                self._vals[current_idx],self._vals[parent_idx]=self._vals[parent_idx],self._vals[current_idx]
                self._d[self._keys[current_idx]] = parent_idx
                self._d[self._keys[parent_idx]] = current_idx
                self._keys[current_idx],self._keys[parent_idx]=self._keys[parent_idx],self._keys[current_idx]
                current_idx=parent_idx
                parent_idx=current_idx//2
            else:
                break

    def _down(self,current):
        current_idx=current
        child_idx=current_idx*2
        self._d[self._keys[current_idx]] = current_idx
        while child_idx<=self._size:
            if child_idx+1<=self._size and self._vals[child_idx+1]<self._vals[child_idx]:
                child_idx=child_idx+1
            if self._vals[child_idx]<self._vals[current_idx]:
                self._vals[current_idx], self._vals[child_idx] = self._vals[child_idx], self._vals[current_idx]
                self._d[self._keys[current_idx]] = child_idx
                self._d[self._keys[child_idx]] = current_idx
                self._keys[current_idx], self._keys[child_idx] = self._keys[child_idx], self._keys[current_idx]
                current_idx=child_idx
                child_idx=current_idx*2
            else:
                break

class SP:
    '''最短路径'''
    def __init__(self,G:EdgeWeightDigraph,s):
        self.s=s
        self._edgeTo=[None for _ in range(G.V())]
        self._distTo=[float('inf') for _ in range(G.V())]
        self._distTo[s]=0.0


    def relax(self, G, v):
        for e in G.adj(v):
            w = e.to()
            if self._distTo[w] > self._distTo[v] + e.weight():
                self._distTo[w] = self._distTo[v] + e.weight()
                self._edgeTo[w] = e

    def pathTo(self,v):
        '''返回s到达v的最短路径边'''
        if self._distTo[v]==float('inf'):
            return None
        else:
            path=[]
            path.append(self._edgeTo[v])
            w=self._edgeTo[v].come()
            while w!=self.s:
                e=self._edgeTo[w]
                path.append(e)
                w=e.come()
            return path[::-1]

    def distTo(self,v):
        '''s到v的最短距离'''
        return self._distTo[v]

    def hasPathTo(self,v):
        return self._distTo[v]!=float('inf')

    def __str__(self):
        s=""
        for v in range(len(self._distTo)):
            if v==self.s:
                continue
            if self.hasPathTo(v):
                p=self.pathTo(v)
                s += "len=%d, weights=%.2f :: %d" % (len(p),self.distTo(v),self.s)
                for e in p:
                    s+="--%.2f-->%d" % (e.weight(),e.to())
                s+='\n'
        return s

class DijkstraSP(SP):
    '''非负加权有向图的最短路径'''
    def __init__(self,G:EdgeWeightDigraph,s):
        super(DijkstraSP,self).__init__(G,s)
        self._pq = IndexMinPQ()
        self._pq.enqueue(s,0.0)
        while len(self._pq):
            v,val=self._pq.dequeue()
            self.relax(G,v)

    def relax(self, G, v):
        for e in G.adj(v):
            w = e.to()
            if self._distTo[w] > self._distTo[v] + e.weight():
                self._distTo[w] = self._distTo[v] + e.weight()
                self._edgeTo[w] = e
                if self._pq.contain(w):
                    self._pq.change(w, self._distTo[w])
                else:
                    self._pq.enqueue(w, self._distTo[w])

from collections import deque
class Topological:
    '''拓扑排序'''
    def __init__(self,G:EdgeWeightDigraph):
        self._order=deque()
        self._marked=[False for _ in  range(G.V())]
        for v in range(G.V()):
            if not self._marked[v]:
                self._dfs(G,v)

    def _dfs(self,G,v):
        self._marked[v]=True
        for e in G.adj(v):
            w=e.to()
            if not self._marked[w]:
                self._dfs(G,w)
        self._order.appendleft(v)

    def order(self):
        return self._order

class AcyclicSP(SP):
    '''无环加权有向图的单元最短路径'''
    def __init__(self,G:EdgeWeightDigraph,s):
        super(AcyclicSP, self).__init__(G,s)
        tp=Topological(G)
        order=tp.order()
        for v in order:
            self.relax(G,v)


class AcyclicLP(SP):
    '''最长路径'''
    def __init__(self,G:EdgeWeightDigraph,s):
        super(AcyclicLP, self).__init__(G,s)
        for i in range(len(self._distTo)):
            self._distTo[i]=float('-inf')
        self._distTo[s]=0.
        tp=Topological(G)
        order=tp.order()
        for v in order:
            self.relax(G,v)

    def relax(self, G, v):
        for e in G.adj(v):
            w=e.to()
            if self._distTo[w]<self._distTo[v]+e.weight():
                self._distTo[w]=self._distTo[v]+e.weight()
                self._edgeTo[w]=e

class CPM:
    '''关键路径'''
    def __init__(self,filename,delim):
        with open(filename) as f:
            N=int(f.readline().strip()) # 任务数
            G=EdgeWeightDigraph(V=2*N+2)
            self.s,self.t=2*N,2*N+1 # 系统起点和系统终点
            for i,line in enumerate(f.readlines()):
                line=line.strip().split(delim)
                time=float(line[0])
                begin=i # 任务起点
                end=i+N # 任务终点
                e=DirectedEdge(begin,end,time)
                G.addEdge(e)
                e=DirectedEdge(self.s,begin,0.)
                G.addEdge(e)
                e=DirectedEdge(end,self.t,0.)
                G.addEdge(e)
                for v in line[1:]:
                    v=int(v)
                    e=DirectedEdge(end,v,0.)
                    G.addEdge(e)

        self._lp=AcyclicLP(G,self.s)

    def distTo(self,i):
        return self._lp.distTo(i)

    def finishTime(self):
        return self._lp.distTo(self.t)

    def cpmPath(self):
        '''关键路径'''
        path=self._lp.pathTo(self.t)
        rPath=[]
        i=1
        while i<len(path):
            rPath.append(path[i].come())
            i+=2
        return rPath



if __name__ == '__main__':
    e=DirectedEdge(1,2,3)
    print(e)
    print(float('nan'))

    minq=IndexMinPQ()
    keys=[0,1,2,3,4,5,6,7]
    vals=[0.1,0.3,0.2,0.5,0.7,0.2,0.4,0.6]
    for k,v in zip(keys,vals):
        minq.enqueue(k,v)
    while len(minq):
        print(minq.dequeue())
    G=EdgeWeightDigraph('./data/tinyEWG.txt',delim=' ')
    sp=DijkstraSP(G,0)
    print(sp)
    ap=AcyclicSP(G,0)
    print(sp)

    cpm=CPM('data/jobsPC.txt',' ')
    for i in range(cpm.s//2):
        print(cpm.distTo(i))
    print('关键路径：',cpm.cpmPath())
    print('完成最短用时：',cpm.finishTime())
