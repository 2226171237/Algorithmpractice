#-*- coding=utf-8-*-
'''
如何判断两颗二叉树是否相等？
两颗二叉树相等是指这两颗二叉树有相同得结构，并且在相同得位置上得节点有相同得指。
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

def isEqual(root1,root2):
    '''
    递归方法
    :param root1:
    :param roo2:
    :return:
    '''
    if root1 is None and root2 is None:
        return True
    if (root1 is None) ^ (root2 is None):
        return False
    if root1.x==root2.x:
        if (isEqual(root1.lchild,root2.lchild) and isEqual(root1.rchild,root2.rchild)):
            return True
        else:
            return False
    return False

if __name__ == '__main__':
    T1=BiTree()
    T2=BiTree()
    arr1 = [1,2,3,4,5,6,7]
    T1.array2tree(arr1)
    arr2 = [1,2,4,5,6,7,8]
    T2.array2tree(arr2)
    print(isEqual(T1.root,T2.root))

