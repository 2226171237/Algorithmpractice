'''
请定义一个队列并实现函数 max_value 得到队列里的最大值，
要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都是O(1)。
若队列为空，pop_front 和 max_value 需要返回 -1

限制：
1 <= push_back,pop_front,max_value的总操作数 <= 10000
1 <= value <= 10^5
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/dui-lie-de-zui-da-zhi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()

from collections import deque

class InternalData:
    def __init__(self,val,index):
        self.val=val
        self.index=index

class MaxQueue(object):
    def __init__(self):
        self._dq=deque()
        self._maxdq=deque()
        self._current_idx=0

    def max_value(self):
        """
        :rtype: int
        """
        if len(self._dq)==0:
            return -1
        return self._maxdq[0].val

    def push_back(self, value):
        """
        :type value: int
        :rtype: None
        """
        while len(self._maxdq) and value>=self._maxdq[-1].val:
            self._maxdq.pop()
        a=InternalData(value,self._current_idx)
        self._dq.append(a)
        self._maxdq.append(a)
        self._current_idx+=1

    def pop_front(self):
        """
        :rtype: int
        """
        if len(self._dq)==0:
            return -1
        if self._maxdq[0].index==self._dq[0].index:
            self._maxdq.popleft()
        return self._dq.popleft().val



if __name__ == '__main__':
    q=MaxQueue()
    q.push_back(2)
    q.push_back(3)
    q.push_back(1)
    q.push_back(4)
    q.push_back(5)
    q.push_back(0)
