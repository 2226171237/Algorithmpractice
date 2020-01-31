# -*- coding=utf-8 -*-
'''
单链表有环是指单链表中某个节点的next域指向的链表中它之前的某一个节点，这样再链表的尾部形成一个环形结构，
如何判断单链表是否有环存在？
'''
class LNode:
    def __init__(self,x,next=None):
        self._data=x
        self.next=next

class LList:
    def __init__(self,data=[]):
        self.head=None
        if data:
            data=list(data)
            for d in data:
                self.push(d)

    def is_empty(self):
        return self.head is None

    def push(self,x):
        if self.is_empty():
            self.head=LNode(x)
        else:
            node=self.head
            while node.next:
                node=node.next
            node.next=LNode(x)

    def visit(self):
        if self.is_empty():
            return
        print('head',end='->')
        node=self.head
        while node:
            print(node._data,end='->')
            node=node.next
        print('end')

    def isLoop1(self):
        '''
        hash set
        :return:
        '''
        if self.is_empty() or self.head.next is None:
            return False
        hash_set=set()
        node=self.head
        while node:
            if node in hash_set:
                return True
            else:
                hash_set.add(node)
            node=node.next
        return False

    def isLoop2(self):
        '''
        快慢指针
        :return:
        '''
        if self.is_empty() or self.head.next is None:
            return False
        slow=self.head
        fast=self.head
        while fast:
            if fast.next is None:
                break
            fast=fast.next.next
            slow=slow.next
            if id(fast)==id(slow):
                return True
        return False

    # 链存在环，如何找到环的入口呢？
    def findLoopNode(self):
        '''
        相遇点和链表起点同时向前一步一步走，首次相遇的节点就是环的入口。
        :return:
        '''
        if self.is_empty() or self.head.next is None:
            return None

        slow=self.head
        fast=self.head
        head=self.head
        # 判断是否有环，并找相遇点
        isloop=False
        while fast:
            if fast.next is None:
                break
            fast=fast.next.next
            slow=slow.next
            if id(fast)==id(slow):
                isloop=True
                break
        # 找环的入口
        if isloop:
            while True:
                if id(head)==id(slow):
                    return slow
                else:
                    head=head.next
                    slow=slow.next
        else:
            return None


if __name__ == '__main__':

    L=LList([1,2,3,4,5,6])
    L.visit()
    node=L.head
    nodeloop=node.next.next   # 3
    while node.next:
        node=node.next
    node.next=LNode(7,nodeloop)
    print(L.isLoop1())
    print(L.isLoop2())
    print(L.findLoopNode()._data)