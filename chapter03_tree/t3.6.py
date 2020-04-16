#-*- coding=utf-8-*-
'''
如何把二叉树转化为双向链表？
输入一棵二元查找树，将该二元查找树转化成一个排序的双向链表。要求不能创建任何新的节点，只能调整节点的指向。
'''
from collections import deque
class BiTNode:
    def __init__(self,x,lchild=None,rchild=None):
        self.x=x
        self.lchild=lchild
        self.rchild=rchild

class BiTree:
    def __init__(self):
        self.root=None
        self.pHead=None
        self.pEnd=None

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

    def change2DoubleList(self):
        '''
        中序遍历方法，转化成双向链表
        :return:
        '''
        if self.is_empty():
            return

        def _change(root):
            if root is None:
                return None
            _change(root.lchild)
            root.lchild=self.pEnd
            if None ==self.pEnd:
                self.pHead=root
            else:
                self.pEnd.rchild=root
            self.pEnd=root
            _change(root.rchild)
        _change(self.root)

if __name__ == '__main__':

    T1=BiTree()
    T1.root=BiTNode(4)
    T1.root.lchild=BiTNode(2)
    T1.root.rchild=BiTNode(6)
    T1.root.lchild.lchild=BiTNode(1)
    T1.root.lchild.rchild=BiTNode(3)
    T1.root.rchild.lchild=BiTNode(5)
    T1.root.rchild.rchild=BiTNode(7)
    T1.bfs()
    T1.change2DoubleList()
    head=T1.pHead
    while head:
        print(head.x,end='->')
        head=head.rchild
    print()

    end = T1.pEnd
    while end:
        print(end.x, end='->')
        end = end.lchild
    print()