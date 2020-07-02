'''
我们把无限数量 ∞ 的栈排成一行，按从左到右的次序从 0 开始编号。每个栈的的最大容量 capacity 都相同。

实现一个叫「餐盘」的类 DinnerPlates：

DinnerPlates(int capacity) - 给出栈的最大容量 capacity。
void push(int val) - 将给出的正整数 val 推入 从左往右第一个 没有满的栈。
int pop() - 返回 从右往左第一个 非空栈顶部的值，并将其从栈中删除；如果所有的栈都是空的，请返回 -1。
int popAtStack(int index) - 返回编号 index 的栈顶部的值，并将其从栈中删除；如果编号 index 的栈是空的，请返回 -1。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/dinner-plate-stacks
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

import heapq

class DinnerPlates(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity=capacity
        self.stacks=[]
        self.q=[]

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        while self.q and self.q[0]<len(self.stacks) and len(self.stacks[self.q[0]])==self.capacity:
            heapq.heappop(self.q)

        if not self.q:
            heapq.heappush(self.q,len(self.stacks))

        if self.q[0]==len(self.stacks):
            self.stacks.append([])

        self.stacks[self.q[0]].append(val)

    def pop(self):
        """
        :rtype: int
        """
        while self.stacks and not self.stacks[-1]:
            self.stacks.pop()

        return self.popAtStack(len(self.stacks)-1)


    def popAtStack(self, index):
        """
        :type index: int
        :rtype: int
        """
        if 0<=index <len(self.stacks) and self.stacks[index]:
            heapq.heappush(self.q,index)
            return self.stacks[index].pop()
        return -1
