# -*- coding=utf-8 -*-
'''
给定链表L0->L1->L2-....->Ln,把链表重新排列为L0->Ln->L1->Ln-1->L2->Ln-2...
要求：
1。 在原来链表的基础上进行排序，即不可以申请新的节点
2. 只能修改节点的next域，不可以修改数据域
'''

class LNode:
    def __init__(self,x,next=None):
        self._data=x
        self.next=None


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


    def findMiddenElem(self):
        if self.is_empty():
            return
        if self.head.next is None:
            return self.head

        slow=self.head
        fast=self.head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        return slow.next

    @staticmethod
    def reversed(head):
        '''
        插入法
        :return:
        '''

        if head is None or head.next is None:
            return head
        parent=head
        current=head.next
        head.next=None
        while current:
            head=current
            current = current.next
            head.next=parent
            parent=head
        return head

    def resorted(self):
        if self.is_empty() or self.head.next is None or self.head.next.next is None:
            return
        mid_node=self.findMiddenElem()
        mid_node=self.reversed(mid_node)

        node1=self.head
        node2=mid_node
        child1 = self.head.next
        child2 = mid_node.next
        while child2:
            node1.next=node2
            node2.next=child1
            node1=child1
            node2=child2
            child1=child1.next
            child2=child2.next
        node1.next=node2
        node2.next=child1
        if child1:
            child1.next=None


if __name__ == '__main__':
    L1=LList([1,2,3,4,5,6,7,8])
    L1.visit()
    print(L1.findMiddenElem()._data)
    L1.resorted()
    L1.visit()