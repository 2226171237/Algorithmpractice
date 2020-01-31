# -*- coding=utf-8 -*-
'''
把链表相邻元素翻转。
如输入：1->2->3->4->5->6->7
输出：  2->1->4->3->6->5->7
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

    def reverse1(self):
        '''
        交换值法，交换相邻的节点的值域
        :return:
        '''
        if self.is_empty() or self.head.next is None:
            return
        current=self.head
        child=self.head.next
        while child:
            temp=current._data
            current._data=child._data
            child._data=temp
            current=child.next
            if current is None:
                break
            child=child.next.next

    def reverse2(self):
        '''
        就地交换
        :return:
        '''
        if self.is_empty() or self.head.next is None:
            return
        pred=self.head
        current=self.head
        child=self.head.next
        self.head=child
        while child:
            pred.next=child
            current.next=child.next
            child.next=current
            pred=current
            current=current.next
            if current is None:
                break
            child=current.next


if __name__ == '__main__':

    L=LList([1,2,3,4,5,6,7,8,9])
    L.visit()
    L.reverse1()
    L.visit()
    L.reverse2()
    L.visit()