#-*- coding=utf-8 -*-
'''
给定一个有序链表，其中每个节点也表示一个有序链表，
实现flatten()函数，该函数将联保扁平化成一个单链表，扁平化后也是有序的链表
'''

class LNode:
    def __init__(self,x,right=None,down=None):
        self._data=x
        self.right=right
        self.down=down

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
        new_node=LNode(x) if not isinstance(x,LList) else x.head
        if self.is_empty():
            self.head=new_node
        else:
            if isinstance(x,LList):
                node=self.head
                while node.right:
                    node=node.right
                node.right=new_node
            else:
                node=self.head
                while node.down:
                    node=node.down
                node.down=LNode(x)

    def visit(self):
        if self.is_empty():
            return
        print('head')
        node=self.head
        while node:
            childnode = node
            while childnode:
                print(childnode._data,end='->')
                childnode=childnode.down
            print('end')
            node=node.right
        print('end')


    def merge(self,a,b):
        '''
        合并有序链表,归并排序中的合并
        :param a:
        :param b:
        :return:
        '''
        if a is None:
            return b
        if b is None:
            return a
        if a._data<b._data:
            result=a
            result.down=self.merge(a.down,b)
        else:
            result=b
            result.down=self.merge(a,b.down)
        return result

    def flatten(self,head):
        if head is None or head.right is None:
            return head

        head.right=self.flatten(head.right)

        head=self.merge(head,head.right)
        return head

if __name__ == '__main__':

    L1=LList([3,6,8,31])
    L2=LList([11,21])
    L3=LList([15,22,50])
    L4=LList([30,39,40,55])
    L=LList([L1,L2,L3,L4])
    L.visit()

    head=L.flatten(L.head)
    node=head
    while node:
        print(node._data,end='->')
        node=node.down
