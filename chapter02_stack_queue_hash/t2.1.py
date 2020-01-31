#-*-coding=utf-8-*-
'''
实现栈。
实现一个栈的数据结构，使其具有以下方法：压栈，弹栈，取栈顶元素，判断栈是否为空以及获取栈中元素个数
'''

# 方法1：使用数组实现
class MyStack1:
    def __init__(self):
        self.items=[]

    def is_empty(self):
        return self.items == []

    def push(self,x):
        self.items.append(x)

    def pop(self):
        return self.items.pop()

    def top(self):
        return self.items[-1]

    def length(self):
        return len(self.items)

# 方法2：使用链表实现
class LNode:
    def __init__(self,x,next=None):
        self._data=x
        self.next=next

class MyStack2:
    def __init__(self):
        self.head=None # 栈顶
        self._length=0

    def is_empty(self):
        return self.head is None

    def push(self,x):
        if self.is_empty():
            self.head=LNode(x)
        else:
            tmp=self.head
            self.head=LNode(x)
            self.head.next=tmp
        self._length+=1

    def pop(self):
        if self.is_empty():
            return None
        node=self.head
        self.head=self.head.next
        self._length-=1
        return node

    def top(self):
        if self.is_empty():
            return None
        return self.head

    def length(self):
        return self._length


if __name__ == '__main__':

    S=MyStack2()
    for i in [2,3]:
        S.push(i)
    print(S.length())
    print(S.pop()._data)
    print(S.pop()._data)
    print(S.length())
    
    S = MyStack1()
    for i in [2, 3]:
        S.push(i)
    print(S.length())
    print(S.pop())
    print(S.pop())
    print(S.length())
    print()
