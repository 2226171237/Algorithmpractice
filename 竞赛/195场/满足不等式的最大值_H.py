'''
给你一个数组 points 和一个整数 k 。数组中每个元素都表示二维平面上的点的坐标，并按照横坐标 x 的值从小到大排序。
也就是说 points[i] = [xi, yi] ，并且在 1 <= i < j <= points.length 的前提下， xi < xj 总成立。

请你找出 yi + yj + |xi - xj| 的 最大值，其中 |xi - xj| <= k 且 1 <= i < j <= points.length。
题目测试数据保证至少存在一对能够满足 |xi - xj| <= k 的点。

提示：
2 <= points.length <= 10^5
points[i].length == 2
-10^8 <= points[i][0], points[i][1] <= 10^8
0 <= k <= 2 * 10^8
对于所有的1 <= i < j <= points.length ，points[i][0] < points[j][0] 都成立。也就是说，xi 是严格递增的。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/max-value-of-equation
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

from collections import deque
class Solution(object):
    def findMaxValueOfEquation(self, points, k):
        """
        yi + yj + xj - xi=xj+yj+(yi-xi),单调队列
        :type points: List[List[int]]
        :type k: int
        :rtype: int
        """
        ans=-2**31
        Q=deque()
        Q.append((points[0][0],points[0][1]-points[0][0]))
        for i in range(1,len(points)):
            while len(Q) and points[i][0]-Q[0][0]>k:
                Q.popleft()
            if len(Q):
                ans=max(ans,points[i][0]+points[i][1]+Q[0])
            # 入队
            while len(Q) and Q[-1][1]<=points[i][1]-points[i][0]:
                Q.pop()
            Q.append((points[i][0],points[i][1]-points[i][0]))
        return ans

