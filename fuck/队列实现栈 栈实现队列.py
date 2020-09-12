

# 堆栈实现队列
class Queue:
    def __init__(self):
        self._stack1=[]
        self._stack2=[]
        self._size=0

    def is_empty(self):
        return self._size==0

    def enqueue(self,x):
        self._stack1.append(x)
        self._size+=1

    def dequeue(self):
        if self.is_empty():
            return
        if len(self._stack2)==0:
            while len(self._stack1):
                self._stack2.append(self._stack1.pop())
        self._size-=1
        return self._stack2.pop()


# 队列现实堆栈
class Stack:
    def __init__(self):
        self._data=Queue()
        self._size=0
        self.top_value=None

    def is_empty(self):
        return self._size==0

    def push(self,x):
        self.top_value=x
        self._data.enqueue(x)
        self._size+=1

    def pop(self):
        if self.is_empty():
            return
        n=self._size
        while n>1:
            t=self._data.dequeue()
            if n==2:
                self.top_value=t
            self._data.enqueue(t)
            n-=1
        self._size-=1
        return self._data.dequeue()

    def top(self):
        if self.is_empty():
            return
        return self.top_value


stack=Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.top())
print(stack.pop())
print(stack.pop())
print(stack.top())
stack.push(4)
stack.push(5)
print(stack.pop())
print(stack.pop())
print(stack.top())
