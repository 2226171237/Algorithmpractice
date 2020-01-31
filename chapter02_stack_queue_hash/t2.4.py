#-*-coding=utf-8-*-
'''
如何根据入栈序列判断可能的出栈序列
输入两个整数序列，其中一个序列表示栈的push() 顺序，判断另一个序列有没有肯是对应的pop 顺序
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


def isPopSerial(push,pop):
    if push is None or pop is None:
        return False
    pushLen=len(push)
    popLen=len(pop)
    if pushLen!=popLen:
        return False
    S=MyStack()
    pop_index=0
    push_index=0
    while push_index<pushLen:
        S.push(push[push_index])
        while not S.is_empty() and S.top()==pop[pop_index]:
            S.pop()
            pop_index+=1
        push_index+=1

    if S.is_empty() and pop_index==push_index:
        return True
    else:
        return False

if __name__ == '__main__':
    print(isPopSerial([1,2,3,4,5],[5,3,4,2,1]))

