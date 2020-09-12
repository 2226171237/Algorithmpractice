'''
给出方程式 A / B = k, 其中 A 和 B 均为用字符串表示的变量， k 是一个浮点型数字。根据已知方程式求解问题，并返回计算结果。
如果结果不存在，则返回 -1.0。

示例 :
给定 a / b = 2.0, b / c = 3.0
问题: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? 
返回 [6.0, 0.5, -1.0, 1.0, -1.0 ]

equations(方程式) = [ ["a", "b"], ["b", "c"] ],
values(方程式结果) = [2.0, 3.0],
queries(问题方程式) = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ].
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/evaluate-division
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Graph:
    def __init__(self,N):
        self.Vs=[dict() for _ in range(N)]
        self.N=N

    def addEdge(self,p,q,v):
        self.Vs[q][p]=v  # p/q
        self.Vs[p][q]=1/v

    def divResult(self,p,q):
        mask = [False for _ in range(self.N)]
        res=[-1]
        def dfs(s,dst,result):
            if s==dst:
                res[0]=result
                return
            mask[s]=True
            for v in self.Vs[s]:
                if not mask[v]:
                    dfs(v,dst,result/self.Vs[s][v])
        dfs(p,q,1)
        return res[0]

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        var_map=dict()
        t=0
        for a,b in equations:
            if a not in var_map:
                var_map[a]=t
                t+=1
            if b not in var_map:
                var_map[b]=t
                t+=1
        G=Graph(t)
        for i,(a,b) in enumerate(equations):
            x=var_map[a]
            y=var_map[b]
            G.addEdge(x,y,values[i])

        result=[]
        for a,b in queries:
            if a not in var_map or b not in var_map:
                result.append(-1)
                continue
            x = var_map[a]
            y = var_map[b]
            t=G.divResult(x,y)
            result.append(t)
        return result

s=Solution()
test=[[["x1","x2"],["x2","x3"],["x1","x4"],["x2","x5"]],
[3.0,0.5,3.4,5.6],
[["x2","x4"],["x1","x5"],["x1","x3"],["x5","x5"],["x5","x1"],["x3","x4"],["x4","x3"],["x6","x6"],["x0","x0"]]]
print(s.calcEquation(*test))


