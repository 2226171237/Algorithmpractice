
from base_sort import BasicSort

class InsertSort(BasicSort):
    def sort(self,arr):
        n=len(arr)
        for i in range(1,n):
            for j in range(i,0,-1):
                if arr[j]<arr[j-1]:
                    self.swap(arr,j,j-1)


from collections import deque
class Solution(object):
    def minNumberOfSemesters(self, n, dependencies, k):
        """
        :type n: int
        :type dependencies: List[List[int]]
        :type k: int
        :rtype: int
        """
        G=[[] for _ in range(n+1)]
        dep=set()
        for x,y in dependencies:
            G[x].append(y)
            dep.add(y)
        for i in range(1,n+1):
            if i not in dep:
                G[0].append(i)

        Q=deque()
        Q.append((0,0))
        result=[0 for _ in range(n)]
        marked=[False for _ in range(n+1)]
        marked[0]=True
        while len(Q):
            x,h=Q.popleft()
            result[h]+=1
            for y in G[x]:
                if not marked[y]:
                    Q.append((y,h+1))
                    marked[y]=True
        T=0
        for x in result[1:]:
            if x%k==0:
                T+=x//k
            else:
                T+=x//k+1
        return int(T)





if __name__ == '__main__':
    s=InsertSort()
    #s.check()

    s=Solution()
    print(s.minNumberOfSemesters(5,[[1,5],[1,3],[1,2],[4,2],[4,5],[2,5],[1,4],[4,3],[3,5],[3,2]],3))
