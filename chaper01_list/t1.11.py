# -*- coding=utf-8 -*-
'''
判断俩个单链表(无环)是否有交叉重合
判断两个单链表是否相交，并找到相交点。
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

def isIntersect1(L1,L2):
    '''
    hash set
    :param L1:
    :param L2:
    :return:
    '''
    node1=L1.head
    node2=L2.head
    hash_set=set()
    while node1:
        hash_set.add(node1)
        node1=node1.next
    while node2:
        if node2 in hash_set:
            return node2
        else:
            node2=node2.next
    return None

def isIntersect2(L1,L2):
    '''
    首尾相接法
    :param L1:
    :param L2:
    :return:
    '''
    # 将 L1的尾节点连到L2的头
    node1=L1.head
    while node1.next:
        node1=node1.next
    node1.next=L2.head
    # 看 L2是否构成环：
    slow=L1.head
    head=L1.head
    fast=L1.head
    isloop=False
    while fast:
        if fast.next is None:
            break
        fast=fast.next.next
        slow=slow.next
        if id(slow)==id(fast):
            isloop=True
            break
    if isloop:
        while True:
            if id(slow)==id(head):
                return slow
            else:
                slow=slow.next
                head=head.next
    return None

def isIntersect3(L1,L2):
    '''
    尾节点法
    :param L1:
    :param L2:
    :return:
    '''
    node1=L1.head
    node2=L2.head
    list1_node_nums,list2_node_nums=0,0
    while node1.next:
        list1_node_nums += 1
        node1=node1.next
    list1_node_nums+=1
    while node2.next:
        list2_node_nums += 1
        node2=node2.next
    list2_node_nums+=1

    # 有相交，求交点
    if id(node1)==id(node2):
        steps=abs(list2_node_nums-list1_node_nums)
        step=0
        # 找最长的链，开始先走steps步
        node=L1.head if list1_node_nums>list2_node_nums else L2.head
        anthor_node=L1.head if list1_node_nums<=list2_node_nums else L2.head
        while node:
            step+=1
            node=node.next
            if step>=steps:
                if id(anthor_node)==id(node):
                    return node
                else:
                    anthor_node=anthor_node.next
    return None



if __name__ == '__main__':

    L1=LList([1,3,6,9])
    L1.visit()
    L2=LList([1,2,3])
    L2.head.next.next.next=L1.head.next.next
    L2.visit()
    # result=isIntersect1(L1,L2)
    # if result:
    #     print(result._data)
    # result = isIntersect2(L1, L2)
    # if result:
    #     print(result._data)

    result = isIntersect3(L1, L2)
    if result:
        print(result._data)