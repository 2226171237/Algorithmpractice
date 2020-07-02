'''
给出一个区间的集合，请合并所有重叠的区间。

示例 1:
输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2:
输入: [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-intervals
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


from functools import cmp_to_key

def compare(a,b):
    if a[0]>b[0]:
        return 1
    else:
        return -1

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals=sorted(intervals,key=cmp_to_key(compare))
        merged=[intervals[0]]
        for x2,y2 in intervals[1:]:
            x1,y1=merged[-1]
            if x1<=x2<=y1: # 合并
                merged.pop()
                x=min(x1,x2)
                y=max(y1,y2)
                merged.append([x,y])
            else:
                merged.append([x2,y2])
        return merged


if __name__ == '__main__':
    s=Solution()
    print(s.merge([[1,9],[2,5],[19,20],[10,11],[12,20],[0,3],[0,1],[0,2]]))

