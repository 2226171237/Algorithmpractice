'''
在由 2D 网格表示的校园里有 n 位工人（worker）和 m 辆自行车（bike），n <= m。所有工人和自行车的位置都用网格上的 2D 坐标表示。
我们需要为每位工人分配一辆自行车。在所有可用的自行车和工人中，我们选取彼此之间曼哈顿距离最短的工人自行车对  (worker, bike) ，
并将其中的自行车分配給工人。如果有多个 (worker, bike) 对之间的曼哈顿距离相同，那么我们选择工人索引最小的那对。
类似地，如果有多种不同的分配方法，则选择自行车索引最小的一对。不断重复这一过程，直到所有工人都分配到自行车为止。

给定两点 p1 和 p2 之间的曼哈顿距离为 Manhattan(p1, p2) = |p1.x - p2.x| + |p1.y - p2.y|。
返回长度为 n 的向量 ans，其中 a[i] 是第 i 位工人分配到的自行车的索引（从 0 开始）。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/campus-bikes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

from collections import defaultdict
class Solution(object):
    def assignBikes(self, workers, bikes):
        """
        :type workers: List[List[int]]
        :type bikes: List[List[int]]
        :rtype: List[int]
        """
        map=defaultdict(list)
        workerUsed=[False for _ in range(len(workers))]
        bikeUsed=[False for _ in range(len(bikes))]

        for i in range(len(workers)):
            for j in range(len(bikes)):
                d=abs(workers[i][0]-bikes[j][0])+abs(workers[i][1]-bikes[j][1])
                map[d].append((i,j))  # 每个d里面就自动有序了

        ans=[0 for _ in range(len(workers))]
        keys=sorted(map.keys())
        for d in keys:
            for i,j in map[d]:
                if workerUsed[i] or bikeUsed[j]:
                    continue
                ans[i]=j
                workerUsed[i]=True
                bikeUsed[j]=True
        return ans

if __name__ == '__main__':
    s=Solution()
    print(s.assignBikes([[0,0],[1,1],[2,0]],[[1,0],[2,2],[2,1]]))