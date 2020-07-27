'''
如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。
如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。

例如，
[2,3,4] 的中位数是 3
[2,3] 的中位数是 (2 + 3) / 2 = 2.5

设计一个支持以下两种操作的数据结构：
void addNum(int num) - 从数据流中添加一个整数到数据结构中。
double findMedian() - 返回目前所有元素的中位数。
示例 1：
输入：
["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]
[[],[1],[2],[],[3],[]]
输出：[null,null,null,1.50000,null,2.00000]
示例 2：
输入：
["MedianFinder","addNum","findMedian","addNum","findMedian"]
[[],[2],[],[3],[]]
输出：[null,null,2.00000,null,2.50000]
 
限制：
最多会对 addNum、findMedia进行 50000 次调用。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-ju-liu-zhong-de-zhong-wei-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

import  heapq

class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.maxHeap=[]
        self.minHeap=[]

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if len(self.maxHeap)==len(self.minHeap):
            heapq.heappush(self.minHeap,num)
            t=heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap,-t)
        else:
            heapq.heappush(self.maxHeap, -num)
            t = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, -t)

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.minHeap)==len(self.maxHeap):
            return (self.minHeap[0]-self.maxHeap[0])/2
        elif len(self.minHeap)>len(self.maxHeap):
            return self.minHeap[0]
        else:
            return -self.maxHeap[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

if __name__ == '__main__':
    s=MedianFinder()
    s.addNum(1)
    s.addNum(2)
    print(s.findMedian())
    s.addNum(3)
    print(s.findMedian())
    s.addNum(3)
    print(s.findMedian())