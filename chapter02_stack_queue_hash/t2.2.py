#-*-coding=utf-8-*-
'''
实现队列
实现一个队列的数据结构，使其具有入队，出队，查看队列首元素，查看队列大小等功能
'''

# 方法1：数组实现
class MyQueue1:
    def __init__(self):
        self.items=[]

    def is_empty(self):
        return len(self.items)==0

    def enqueue(self,x):
        self.items.append(x)

    def dequeue(self):
        return self.items.pop(0)

    def getFront(self):
        return self.items[0]

    def getBack(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


# 方法2: 链表实现
class LNode:
    def __init__(self,x,next=None):
        self._data=x
        self.next=next

class MyQueue2:
    def __init__(self):
        self.Front=None
        self.Back=None
        self._length=0

    def is_empty(self):
        return self._length==0

    def enqueue(self,x):
        if self.is_empty():
            self.Front=self.Back=LNode(x)
        else:
            self.Back.next=LNode(x)
            self.Back=self.Back.next
        self._length+=1

    def dequeue(self):
        if self.is_empty():
            return None
        node=self.Front
        self.Front= self.Front.next
        self._length-=1
        return node._data

    def getFront(self):
        if self.Front:
            return self.Front._data

    def getBack(self):
        if self.Back:
            return self.Back._data

    def size(self):
        return self._length

if __name__ == '__main__':
    Q1=MyQueue1()
    for i in [1,2,3,4,5]:
        Q1.enqueue(i)
    print(Q1.dequeue())
    print(Q1.dequeue())
    print(Q1.size())

    Q1 = MyQueue2()
    for i in [1, 2, 3, 4, 5]:
        Q1.enqueue(i)
    print(Q1.dequeue())
    print(Q1.dequeue())
    print(Q1.size())

