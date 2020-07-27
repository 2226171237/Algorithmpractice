# 栈实现队列
class Queue:
    def __init__(self):
        self._stack1=[]
        self._stack2=[]
        self._size=0

    def size(self):
        return self._size

    def is_empty(self):
        return self._size==0

    def enqueue(self,x):
        self._stack1.append(x)
        self._size+=1

    def dequeue(self):
        if self.is_empty():
            return -1
        if len(self._stack2)==0:
            while len(self._stack1):
                self._stack2.append(self._stack1.pop())
        self._size-=1
        return self._stack2.pop()

# 队列实现栈,一个队列就可以实现
from collections import deque
class Stack:
    def __init__(self):
        self._queue=deque()
        self._size=0
        self.tail=-1

    def size(self):
        return self._size

    def is_empty(self):
        return self._size==0

    def push(self,x):
        self.tail=x
        self._queue.append(x)
        self._size+=1

    def pop(self):
        if self.is_empty():
            return -1
        size=self._size
        while size>2:
            t=self._queue.popleft()
            self._queue.append(t)
            size-=1
        self._size -= 1
        if self.is_empty():
            self.tail=-1
        else:
            self.tail=self._queue.popleft()
            self._queue.append(self.tail)
        return self._queue.popleft()

    def peek(self):
        return self.tail

if __name__ == '__main__':
    stack=Stack()
    arr=[1,2,3,4,5,6]
    for x in arr:
        stack.push(x)
    while stack.size()>0:
        print(stack.pop(),end=' ')
    print()

    Q=Queue()
    for x in arr:
        Q.enqueue(x)
    while Q.size()>0:
        print(Q.dequeue(),end=' ')
    print()


