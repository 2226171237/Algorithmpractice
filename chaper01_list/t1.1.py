# -*- coding=utf-8 -*-
'''
给定一个带头节点的单链表，请将其逆序。即：单链表原来为：head->1->2->3->4->5->6->7
逆序后变为：head->7->6->5->4->3->2->1。
'''

class LNode:
    def __init__(self,x):
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
        return  self.head is None

    def push(self,x):
        if self.is_empty():
            self.head=LNode(x)
        else:
            parent=self.head
            child=self.head.next
            while child:
                parent=child
                child=child.next
            parent.next=LNode(x)

    def visit(self):
        if self.is_empty():
            return
        parent=self.head
        print('head',end='->')
        while parent:
            print(parent._data,end='->')
            parent=parent.next
        print('null')


    def reversed1(self):
        if self.is_empty():
            return
        datas=[]
        parent=self.head
        while parent:
            datas.append(parent._data)
            parent=parent.next

        i=-1
        parent = self.head
        while parent:
            parent._data=datas[i]
            parent = parent.next
            i-=1

    def reversed2(self):
        '''
        就地逆序
        :return:
        '''
        if self.is_empty():
            return
        parent=None
        current=self.head
        child=current.next
        while True:
            current.next=parent
            parent=current
            current=child
            if current is None:
                break
            child=current.next
        self.head=parent

    def reversed3(self):
        '''
        递归实现
        :return:
        '''

        if self.is_empty() or self.head.next is None:
            return

        def re_reversed(node):
            if node.next is None or node is None:
                return node
            self.head=node.next
            node_t=re_reversed(node.next)
            node_t.next=node
            node.next=None
            return node
        re_reversed(self.head)

    def reversed4(self):
        '''
        插入法
        :return:
        '''

        if self.is_empty() or self.head.next is None:
            return
        parent=self.head
        current=self.head.next
        self.head.next=None 
        while current:
            self.head=current
            current = current.next
            self.head.next=parent
            parent=self.head



if __name__ == '__main__':
    list1=LList([1,2,3,4,5,6])
    list1.push(7)
    list1.visit()
    list1.reversed1()
    list1.visit()
    list1.reversed2()
    list1.visit()
    list1.reversed3()
    list1.visit()
    list1.reversed4()
    list1.visit()