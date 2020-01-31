# -*- coding=utf-8 -*-
'''
给定一个没有排序的连表，去掉其重复项，并保留原顺序，
例如：链表 1->3->1->5->5->7,得到：1->3->5->7
'''

class LNode:
    def __init__(self,x,next=None):
        self._data=x
        self.next=next


class  LList:
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

    def removeDup1(self):
        '''
        hash set
        :return:
        '''
        if self.is_empty() or self.head.next is None:
            return
        hash_set=set()

        node=self.head
        parent=self.head
        while node:
            if node._data in hash_set:
                # 删除重复节点
                parent.next=node.next
            else:
                hash_set.add(node._data)
            parent=node
            node=node.next

    def removeDup2(self):
        '''
        双重循环遍历
        :return:
        '''
        if self.head.next is None or self.is_empty():
            return

        node=self.head
        while node:
            parent=node
            child=node.next
            while child:
                if child._data==node._data:
                    parent.next=child.next
                parent=child
                child=child.next
            node=node.next

    def removeDup3(self):
        '''
        递归
        :return:
        '''
        if self.head.next is None or self.is_empty():
            return

        def re_removeDup(head):
            if head is None or head.next is None:
                return head
            # 删除子链重复节点
            head.next=re_removeDup(head.next)
            # 删除子链中，与head相同的节点
            node=head.next
            parent=head
            while node:
                if node._data==head._data:
                    parent.next=node.next
                parent=node
                node=node.next
            return head
        re_removeDup(self.head)

if __name__ == '__main__':

    L=LList([1,3,1,5,5,7,7])
    L.visit()
    L.removeDup3()
    L.visit()