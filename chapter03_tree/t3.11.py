#-*- coding=utf-8-*-
'''
如何对二叉树进行镜像反转。
'''
from collections import deque
import math
class Stack:
    def __init__(self):
        self.items=[]

    def is_empty(self):
        return len(self.items)==0

    def push(self,x):
        self.items.append(x)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return
        return self.items[-1]

    def size(self):
        return len(self.items)

class BiTNode:
    def __init__(self,x,lchild=None,rchild=None):
        self.x=x
        self.lchild=lchild
        self.rchild=rchild

class BiTree:
    def __init__(self):
        self.root=None
        self.num=1

    def is_empty(self):
        return self.root is None

    def bfs(self):
        '''
        层次遍历
        :return:
        '''
        if self.is_empty():
            return
        root=self.root
        q=deque()
        q.append(root)
        while len(q)>0:
            node=q.popleft()
            print(node.x,end='->')
            if node.lchild:
                q.append(node.lchild)

            if node.rchild:
                q.append(node.rchild)
        print()

    def array2tree(self,arr):

        def _array2tree(arr,begin,end):
            if begin>end:
                return None
            mid=(begin+end+1)//2
            root=BiTNode(arr[mid])
            root.lchild=_array2tree(arr,begin,mid-1)
            root.rchild=_array2tree(arr,mid+1,end)
            return root
        self.root=_array2tree(arr,0,len(arr)-1)

    def reverseTree(self):

        def _reverseTree(root):
            if root is None:
                return None
            _reverseTree(root.lchild)
            _reverseTree(root.rchild)
            tmp=root.lchild
            root.lchild=root.rchild
            root.rchild=tmp

        _reverseTree(self.root)
        
if __name__ == '__main__':

    T1=BiTree()
    node1 = BiTNode(1)
    node2 = BiTNode(2)
    node3 = BiTNode(3)
    node4 = BiTNode(4)
    node5 = BiTNode(5)
    node6 = BiTNode(6)
    node7 = BiTNode(7)
    node8 = BiTNode(8)
    node9 = BiTNode(9)
    T1.root=node1
    T1.root.lchild=node2
    T1.root.rchild=node3
    T1.root.lchild.lchild=node5
    T1.root.lchild.rchild=node8
    T1.root.lchild.rchild.lchild=node9
    T1.root.lchild.rchild.rchild=node7
    T1.root.rchild.rchild=node4
    T1.root.rchild.rchild.lchild=node6
    T1.bfs()

    T1.reverseTree()
    T1.bfs()