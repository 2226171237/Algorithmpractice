#-*- coding=utf-8-*-
'''
如何判断一个数组是否是二元查找树后序遍历的序列。
输入一个整数数组，判断该数组是否是某二元查找树的后序遍历结果。如果是，那么返回True,
否则返回False。

二元查找树：对任意节点，它的左子树上所有节点的值都小于这个节点的值，右子树上所有节点的值都大于这个节点的值。
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

def isAfterOrder(arr,begin,end):
    if len(arr)==0:
        return False
    root=arr[end]
    i=begin
    while i<end:
        if arr[i]>=root:
            break
        i+=1
    j=i
    while j<end:
        if arr[j]<root:
            return False
        j+=1
    l_ok=True
    r_ok=True
    if i>begin:
        l_ok=isAfterOrder(arr,begin,i-1)
    if i<end:
        r_ok=isAfterOrder(arr,i,end-1)
    if l_ok and r_ok:
        return True

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
    arr=[1,3,2,5,7,6]
    print(isAfterOrder(arr,0,len(arr)-1))
