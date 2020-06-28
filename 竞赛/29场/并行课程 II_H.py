'''
给你一个整数 n 表示某所大学里课程的数目，编号为 1 到 n ，数组 dependencies 中， 
dependencies[i] = [xi, yi]  表示一个先修课的关系，也就是课程 xi 必须在课程 yi 之前上。同时你还有一个整数 k 。
在一个学期中，你 最多 可以同时上 k 门课，前提是这些课的先修课在之前的学期里已经上过了。
请你返回上完所有课最少需要多少个学期。题目保证一定存在一种上完所有课的方式。

提示：
1 <= n <= 15
1 <= k <= n
0 <= dependencies.length <= n * (n-1) / 2
dependencies[i].length == 2
1 <= xi, yi <= n
xi != yi
所有先修关系都是不同的，也就是说 dependencies[i] != dependencies[j] 。
题目输入的图是个有向无环图。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/parallel-courses-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''



from collections import deque
class Solution(object):
    def minNumberOfSemesters(self, n, dependencies, k):
        """
        拓扑排序
        :type n: int
        :type dependencies: List[List[int]]
        :type k: int
        :rtype: int
        """
        G=[[] for _ in range(n)]
        prev=[[] for _ in range(n)]
        for x,y in dependencies:
            G[x-1].append(y-1)
            prev[y-1].append(x-1)

        marked=[False for _ in range(n)]
        order=[]
        def dfs(G,x):
            marked[x]=True
            for y in G[x]:
                if not marked[y]:
                    dfs(G,y)
            order.append(x)
        for x in range(n):
            if not marked[x]:
                dfs(G,x)
        T=0
        order=order[::-1]
        order=[i for i in range(n)]
        Q=deque()
        has_learn=0
        marked=[False for _ in range(n)]
        while has_learn<n:
            for x in order:
                if len(prev[x])==0 and marked[x]==False and x not in Q:
                    if len(G[x])!=0:
                        Q.appendleft(x) # 尽量先选有依赖关系的课程
                    else:
                        Q.append(x)
            m=0
            while m<k and len(Q):
                x=Q.popleft()
                marked[x]=True
                has_learn+=1
                m+=1
                for y in G[x]:
                    if x in prev[y]:
                        prev[y].remove(x)
            T+=1
        return T

if __name__ == '__main__':
    s=Solution()
    print(s.minNumberOfSemesters(11,[],2))




