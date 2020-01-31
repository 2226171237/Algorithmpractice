#-*-coding=utf-8-*-
'''
如何用O(1)的时间复杂度求栈中最小的元素

'''
class LNode:
    def __init__(self, x, next=None):
        self._data = x
        self.next = next


class MyStack:
    def __init__(self):
        self.head = None  # 栈顶
        self._length = 0

    def is_empty(self):
        return self.head is None

    def push(self, x):
        if self.is_empty():
            self.head = LNode(x)
        else:
            tmp = self.head
            self.head = LNode(x)
            self.head.next = tmp
        self._length += 1

    def pop(self):
        if self.is_empty():
            return None
        node = self.head
        self.head = self.head.next
        self._length -= 1
        return node._data

    def top(self):
        if self.is_empty():
            return None
        return self.head._data

    def length(self):
        return self._length

# 方法：使用两个栈，一个栈村原始数据，另一个栈村最小值
class Stack:
    def __init__(self):
        self.stack=MyStack()
        self.min_stack=MyStack()  # 栈低存放当前栈的最小值

    def is_empty(self):
        return self.stack.is_empty()

    def push(self,x):
        if self.is_empty():
            self.min_stack.push(x)
        else:
            min=self.min_stack.top()
            if min>x:
                self.min_stack.push(x)
            else:
                self.min_stack.push(min)
        self.stack.push(x)
    def pop(self):
        self.min_stack.pop()
        return self.stack.pop()

    def size(self):
        return self.stack.length()

    def getMin(self):
        if self.is_empty():
            return
        else:
            return self.min_stack.top()

if __name__ == '__main__':
    S=Stack()
    for x in [9,4,3,2,3,10]:
        S.push(x)
    print(S.getMin())
    S.pop()
    print(S.getMin())
    S.pop()
    print(S.getMin())
    S.pop()
    print(S.getMin())
    S.pop()
    print(S.getMin())
    S.pop()
    print(S.getMin())