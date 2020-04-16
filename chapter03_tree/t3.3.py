#-*- coding=utf-8-*-
'''
如何从根部开始逐层打印二叉树节点数据。

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

    def dfs_midOrder(self):
        '''
        中序遍历， 左->根->右
        :return:
        '''
        if self.is_empty():
            return
        def midOrder(root):
            if root is None:
                return
            midOrder(root.lchild)
            print(root.x,end='->')
            midOrder(root.rchild)
        midOrder(self.root)
        print()

if __name__ == '__main__':
    T=BiTree()
    arr=[1,2,3,4,5,6,7,8,9,10]
    T.array2tree(arr)
    T.bfs()