# -*- coding=utf-8 -*-
'''
给定两个单链表，链表的每个节点代表一位数，计算两个数的和。
如：输入链表(3->1->5)和链表(5->9->2) 输出：8->0->8 ,即513+295=808,注意各位在链表头
'''

class LNode:
    def __init__(self,x,next=None):
        self._data=x
        self.next=next


def fc_add(a,b,c):
    s=a+b+c
    return s%10,s//10  # s,c 和与进位

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

    def add(self,L2):
        SumList=LList()
        node1=self.head
        node2=L2.head
        s,c=0,0
        while node1 and node2:
            s,c=fc_add(node1._data,node2._data,c)
            SumList.push(s)
            node1=node1.next
            node2=node2.next

        node=node1 if node1 else node2
        while node:
            s,c=fc_add(node._data,0,c)
            SumList.push(s)
            node=node.next
        if c:
            SumList.push(c)
        return SumList

if __name__ == '__main__':
    L1=LList([3,4,5,6,7,8])
    L1.visit()
    L2 = LList([9,8,7,6,5])
    L2.visit()

    SumList=L1.add(L2)
    SumList.visit()