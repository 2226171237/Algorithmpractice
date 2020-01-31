#-*-coding=utf-8-*-
'''
如何用两个栈模拟队列操作。
'''
class LNode:
    def __init__(self, x, next=None):
        self._data = x
        self.next = next


class Stack:
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

    def size(self):
        return self._length

class StackQueue:
    def __init__(self):
        self.in_stack=Stack()
        self.out_stack=Stack()

    def is_empty(self):
        return self.in_stack.is_empty() and self.out_stack.is_empty()

    def push(self,x):
        self.in_stack.push(x)

    def pop(self):
        if self.is_empty():
            return
        if self.out_stack.is_empty():
            while not self.in_stack.is_empty():
                self.out_stack.push(self.in_stack.pop())
        return self.out_stack.pop()

    def size(self):
        return self.in_stack.size()+self.out_stack.size()

if __name__ == '__main__':
    S=StackQueue()
    for x in [9,4,3]:
        S.push(x)
    for i in range(S.size()):
        print(S.pop(),end='->')
    S.push(12)
    S.push(13)
    print(S.pop())

