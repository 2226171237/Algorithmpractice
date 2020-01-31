# -*- coding=utf-8 -*-
'''
假设给定链表1->2->3->4->5->6->7 中指向5的指针，要求把5这个节点删除，
得到 1->2->3->4->6->7
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

    def removeNode(self,node):
        '''
        尾节点不可删除，不是尾节点则将其赋值为后继节点，并删除后继节点
        :param node:
        :return:
        '''
        if node is None or node.next is None:
            return False
        next_node=node.next
        node._data=next_node._data
        node.next=next_node.next
        del next_node
        return True

    def insertNode(self,node,x):
        '''
        在节点node前插入一个节点，数据域为x，
        先在node后插入一个节点，然后交换数据域就可以了
        :param node:
        :param x:
        :return:
        '''
        new_node=LNode(x)
        new_node.next=node.next
        node.next=new_node
        tmp=node._data
        node._data=new_node._data
        new_node._data=tmp


if __name__ == '__main__':

    L1=LList([1,3,6,9])
    L1.visit()

    L1.removeNode(L1.head.next)
    L1.visit()
    L1.insertNode(L1.head.next,10)
    L1.insertNode(L1.head.next, 20)
    L1.visit()