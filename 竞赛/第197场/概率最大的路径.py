'''
给你一个由 n 个节点（下标从 0 开始）组成的无向加权图，该图由一个描述边的列表组成，
其中 edges[i] = [a, b] 表示连接节点 a 和 b 的一条无向边，且该边遍历成功的概率为 succProb[i] 。

指定两个节点分别作为起点 start 和终点 end ，请你找出从起点到终点成功概率最大的路径，并返回其成功概率。
如果不存在从 start 到 end 的路径，请 返回 0 。只要答案与标准答案的误差不超过 1e-5 ，就会被视作正确答案。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/path-with-maximum-probability
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Edge:
    def __init__(self,v,w,prob):
        self.v=v
        self.w=w
        self.prob=prob

    def anthor(self,v):
        if self.v==v:
            return self.w
        if self.w==v:
            return self.v
class Node:
    def __init__(self,v,p):
        self.v=v
        self.p=p

    def __lt__(self, other):
        return self.p>other.p

    def __gt__(self, other):
        return self.p<other.p

import heapq

class Solution(object):
    def maxProbability(self, n, edges, succProb, start, end):
        """
        BFS+优先队列
        :type n: int
        :type edges: List[List[int]]
        :type succProb: List[float]
        :type start: int
        :type end: int
        :rtype: float
        """
        G=[[] for _ in range(n)]
        for (a,b),p in zip(edges,succProb):
            edge=Edge(a,b,p)
            G[a].append(edge)
            G[b].append(edge)
        marked=[False for _ in range(n)]

        def bfs(G,start,end):
            Q=[Node(start,1)]
            heapq.heapify(Q)
            while len(Q):
                node=heapq.heappop(Q)
                if marked[node.v]:continue
                if node.v==end:return node.p
                marked[node.v]=True
                for e in G[node.v]:
                    w=e.anthor(node.v)
                    if not marked[w]:
                        heapq.heappush(Q,Node(w,node.p*e.prob))
            return 0.

        return bfs(G,start,end)




if __name__ == '__main__':
    s=Solution()
    print(s.maxProbability(n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, end = 2))



