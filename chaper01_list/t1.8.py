# -*- coding=utf-8 -*-
'''
K链表翻转是指把K个相邻的节点看成一组进行翻转，如果剩余节点不足K个，则保持不变。
假设给定链表 1->2->3->4->5->6->7和一个K=2,那么翻转后的链表为
2->1->4->3->6->5->7
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

    @staticmethod
    def reverse(head):
        if head is None or head.next is None:
            return head

        last_node=head
        pred=head
        current=head.next
        while current:
            head=current
            last_node.next=current.next
            current.next=pred
            pred=current
            current=last_node.next
        return head

    def reverse_k(self,k):
        if self.is_empty() or self.head.next is None:
            return None
        pred=self.head
        begin=self.head
        end=self.head
        step=1
        first=True
        while end:
            end=end.next
            step += 1
            if end is None:
                break
            if step==k:
                step=1
                pNext=end.next
                end.next=None
                if first:
                    self.head=self.reverse(begin)
                    first=False
                else:
                    pred.next=self.reverse(begin)
                pred=begin
                begin=pNext
                end=begin
        pred.next=begin

if __name__ == '__main__':

    L=LList([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17])
    L.visit()
    L.reverse_k(3)
    L.visit() 
