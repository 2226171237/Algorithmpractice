
# 986. 区间列表的交集
# 给定两个由一些 闭区间 组成的列表，每个区间列表都是成对不相交的，并且已经排序。
# 返回这两个区间列表的交集。
#
# （形式上，闭区间 [a, b]（其中 a <= b）表示实数 x 的集合，而 a <= x <= b。两个闭区间的交集是一组实数，要么为空集，
# 要么为闭区间。例如，[1, 3] 和 [2, 4] 的交集为 [2, 3]。）
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/interval-list-intersections
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        union=[]
        i=0
        j=0
        while i<len(A) and j<len(B):
            a1,a2=A[i]
            b1,b2=B[j]
            if not (a1>b2 or b1>a2): # 相交
                x=max(a1,b1)
                y=min(a2,b2)
                union.append([x,y])
            if a2>b2:
                j+=1
            else:
                i+=1
        return union



