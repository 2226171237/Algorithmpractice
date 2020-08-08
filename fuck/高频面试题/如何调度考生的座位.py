

class Edge:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __gt__(self, other):
        if self.y-self.x==other.y-other.x:
            return self.x<other.x
        return self.y-self.x<other.y-other.x

    def __lt__(self, other):
        if self.y - self.x ==other.y - other.x:
            return self.x>other.x
        return self.y - self.x > other.y - other.x

    def distense(self):
        if self.x==-1:
            return self.y
        if self.y==N:
            return N-self.x-1
        return (self.y-self.x)//2

import heapq
class ExamRoom:
    def __init__(self,N):
        self.N=N
        self.left_map=dict()  # 左端点映射到线段
        self.right_map=dict() # 右端点映射到线段
        self._edges=[] # 大顶堆
        edge=Edge(-1,N) # 虚拟线段
        self.left_map[-1]=edge
        self.right_map[N]=edge
        self._edges.append(edge)

    def removeEdge(self,e):
        x=e.x
        y=e.y
        self.left_map.pop(x)
        self.right_map.pop(y)
        self._edges.remove(e)
        heapq.heapify(self._edges)

    def addEdge(self,e):
        x=e.x
        y=e.y
        self.left_map[x]=e
        self.right_map[y]=e
        heapq.heappush(self._edges,e)

    def seat(self):
        longest=heapq.heappop(self._edges)
        x=longest.x
        y=longest.y
        if x==-1:
            s=0
        elif x==self.N:
            s=self.N-1
        else:
            s=(y-x)//2+x
        left=Edge(x,s)
        right=Edge(s,y)
        self.removeEdge(longest)
        self.addEdge(left)
        self.addEdge(right)
        return s

    def leave(self,p):
        left=self.left_map[p.x]
        right=self.right_map[p.y]
        merge=Edge(left.x,right.y)
        self.removeEdge(left)
        self.removeEdge(right)
        self.addEdge(merge)
