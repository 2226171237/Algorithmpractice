# -*-coding=utf-8-*-
'''
如何翻转栈的所有元素？
如：输入栈{1，2，3，4，5}，其中1位于栈顶，则输出为{5,4,3,2,1} ,5在栈顶。
'''


class LNode:
    def __init__(self, x, next=None):
        self._data = x
        self.next = next


class MyStack:
    def __init__(self):
        self.head = None  # 栈顶
        self._length = 0

    def is_empty(self):
        return self.head is None

    def push(self, x):
        if self.is_empty():
            self.head = LNode(x)
        else:
            tmp = self.head
            self.head = LNode(x)
            self.head.next = tmp
        self._length += 1

    def pop(self):
        if self.is_empty():
            return None
        node = self.head
        self.head = self.head.next
        self._length -= 1
        return node._data

    def top(self):
        if self.is_empty():
            return None
        return self.head._data

    def length(self):
        return self._length

    def reversed1(self):
        '''
        送入新的栈
        :return:
        '''
        S=MyStack()
        x=self.pop()
        while x:
            S.push(x)
            x=self.pop()
        return S

    @staticmethod
    def moveButtom2Top(head):
        '''
        将栈低元素，移到栈顶
        :return:
        '''
        if head is None or head.next is None:
            return head
        node=head
        pred=head
        while node.next:
            pred=node
            node=node.next
        pred.next=None
        node.next=head
        head=node
        return head

    def reversed2(self):
        '''
        递归实现
        递归定义：将当前栈低元素移到栈顶，然后其余元素一次下移
        '''
        if self.is_empty() or self.head.next is None:
            return

        def _reversed(head):
            if head is None:
                return head
            head=self.moveButtom2Top(head)
            head.next=_reversed(head.next)
            return head

        self.head=_reversed(self.head)


if __name__ == '__main__':

    S = MyStack()
    for x in [2,6,4,5,3,0,9,6,5,7,0,8]:
        S.push(x)
    S.reversed2()
    print()
