# -*- coding=utf-8 -*-
'''
已知两个链表head1,head2,各自有序，请把他们合并成一个链表，合并后仍然有序。
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


def merge_list(head1,head2):
    result=LList()
    node1=head1.head
    node2=head2.head
    pred_node = result.head
    first=True
    while node1:
        if node2 is None:
            break
        if node1._data<node2._data:
            if first:
                result.head=LNode(node1._data)
                pred_node = result.head
                first=False
            else:
                pred_node.next=LNode(node1._data)
                pred_node=pred_node.next
            node1 = node1.next
        else:
            if first:
                result.head=LNode(node2._data)
                pred_node = result.head
                first=False
            else:
                pred_node.next=LNode(node2._data)
                pred_node=pred_node.next
            node2=node2.next

    node = node1 if node1 else node2
    while node:
        if result.is_empty():
            result.head = LNode(node._data)
            pred_node = result.head
        else:
            pred_node.next=LNode(node._data)
            pred_node = pred_node.next
        node=node.next

    return result



if __name__ == '__main__':

    L1=LList([1,3,6,9])
    L1.visit()
    L2 = LList([4,7,9,10,14])
    L2.visit()
