#-*- coding=utf-8-*-
'''
如何求得一棵二叉树得最大子数和。
给定一棵二叉树，他的每个节点都是正整数或负整数，如何找到一颗子树，使得它所有节点得和最大？
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
        self.maxSum=-2**31

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

    def dfs_aftOder(self):
        '''
        后序遍历
        :return:
        '''
        if self.is_empty():
            return

        def aftOrder(root):
            if root is None:
                return
            aftOrder(root.lchild)
            aftOrder(root.rchild)
            print(root.x,end='->')
        aftOrder(self.root)
        print()

    def findMaxSunTree(self,maxSubTree):
        def _findMaxSunTree(root,maxSubTree):
            if root is None:
                return 0
            lsum=_findMaxSunTree(root.lchild,maxSubTree)
            rsum=_findMaxSunTree(root.rchild,maxSubTree)
            sum=lsum+rsum+root.x
            if sum>self.maxSum:
                self.maxSum=sum
                maxSubTree.x=root.x
            return sum
        _findMaxSunTree(self.root,maxSubTree)
        return self.maxSum
if __name__ == '__main__':
    T=BiTree()
    T.root=BiTNode(6)
    T.root.lchild=BiTNode(3)
    T.root.rchild=BiTNode(-7)
    T.root.lchild.lchild=BiTNode(-1)
    T.root.lchild.rchild=BiTNode(9)
    T.bfs()
    T.dfs_aftOder()

    subTree=BiTNode(0)
    print(T.findMaxSunTree(subTree),subTree.x)