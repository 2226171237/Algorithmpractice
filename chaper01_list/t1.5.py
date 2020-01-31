# -*- coding=utf-8 -*-
'''
找出单链表中，倒数第k个元素。
例：1-2->3->4->5->6->7 第k=3的元素为5
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

    def find_tail_k_elem1(self,k):
        if self.is_empty():
            return
        num=1
        begin=self.head
        end=self.head
        while end.next:
            if num<k:
                end=end.next
                num += 1
            if num==k and end.next:
                end=begin.next
                begin=begin.next
                num=1
        if num==k:
            return begin
        else:
            return None

    def find_tail_k_elem2(self,k):
        '''
        两次循环
        :param k:
        :return:
        '''
        if self.is_empty():
            return None

        # 第一次遍历求个数
        num=0
        node=self.head
        while node:
            num+=1
            node=node.next
        node=self.head

        # 第二次遍历到num-k
        step=0
        while node:
            step+=1
            if step==num-k+1:
                return node
            else:
                node=node.next
        return None

    def find_tail_k_elem3(self,k):
        '''
        双指针,一个指针先走k步，然后两个指针再一起走
        :param k:
        :return:
        '''
        if self.is_empty():
            return None
        pointer_slow=self.head
        node=self.head
        step=0
        while node:
            step+=1
            node=node.next
            if step>k:
                pointer_slow=pointer_slow.next
        return pointer_slow

    def rorate_k(self,k):
        '''
        将单链表向右旋转k个位置
        如：1->2->3->4->5->6->7 k=3 输出：5->6->7->1->2->3->4
        :param k:
        :return:
        '''
        if self.is_empty() or self.head.next is None:
            return None

        slow=self.head
        fast=self.head
        step=0
        while fast.next:
            step+=1
            fast=fast.next
            if step>k:
                slow=slow.next
        fast.next=self.head
        self.head=slow.next
        slow.next=None

if __name__ == '__main__':
    L=LList([1,2,3,4,5,6,7])
    L.visit()
    result=L.find_tail_k_elem1(5)
    if result:
        print(result._data)

    result = L.find_tail_k_elem2(5)
    if result:
        print(result._data)

    result = L.find_tail_k_elem3(5)
    if result:
        print(result._data)

    L.rorate_k(3)
    L.visit()