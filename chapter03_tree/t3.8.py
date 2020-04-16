#-*- coding=utf-8-*-
'''
如何找出排序二叉树上任意两个节点的最近共同父节点。

二元查找树(排序二叉树，搜索二叉树)：对任意节点，它的左子树上所有节点的值都小于这个节点的值，右子树上所有节点的值都大于这个节点的值。
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

    def getPathFromRoot(self,node,s):
        '''
        获取从根节点到node的路径
        :param node:
        :return:
        '''

        def _getPath(root,s):
            if root is None:
                return False
            if root==node:
                s.push(root)
                return True
            if _getPath(root.lchild,s) or _getPath(root.rchild,s):
                s.push(root)
                return True
            return False
        return _getPath(self.root,s)

    def findComParent1(self,node1,node2):
        '''
        方法1：路径对比法
        :param node1:
        :param node2:
        :return:
        '''
        s1=Stack()
        s2=Stack()
        self.getPathFromRoot(node1,s1)
        self.getPathFromRoot(node2,s2)
        comParent=None
        while s1.peek()==s2.peek():
            comParent=s1.peek()
            s1.pop()
            s2.pop()
        return comParent


    def getNodeNum(self,node):
        # 获取node的编号
        self.num=1
        def _getNum(root,num):  # root , root的编号
            if root is None:
                return False
            if root==node:
                return True
            tmp=self.num
            self.num *= 2
            if _getNum(root.lchild,self.num): # 在左子树，则 root.lchild的变换为*2倍
                return True
            else:
                self.num=tmp*2+1
                if _getNum(root.rchild,self.num):
                    return True
            return False
        _getNum(self.root,self.num)

        return self.num

    def findComParent2(self,node1,node2):
        '''
        节点编号法
        :param node1:
        :param node2:
        :return:
        '''
        num1=self.getNodeNum(node1)
        num2=self.getNodeNum(node2)
        #找共同父节点的编号
        while num1!=num2:
            if num1>num2:
                num1//=2
            if num2>num1:
                num2//=2
        parentNum=num1
        #根据父节点的编号，找节点
        root=self.root
        level=int(math.log(parentNum,2))+1
        if level>2:
            level-=2
            while level>=0:
                x=(parentNum>>level) & 1
                if x:
                    root=root.rchild
                else:
                    root=root.lchild
                level-=1
        elif level==2:
            x = (parentNum) & 1
            if x:
                root = root.rchild
            else:
                root = root.lchild

        return root

    def findComParent3(self, node1, node2):
        '''
        后序遍历法
        :param node1:
        :param node2:
        :return:
        '''
        def _findParent(root,node1,node2):
            if None==root or root==node1 or root==node2:
                return root

            lchild=_findParent(root.lchild,node1,node2)  # 左子树有没有node1或node2
            rchild=_findParent(root.rchild,node1,node2)  # 右子树有没有node1或node2
            if None==lchild:
                return rchild
            elif None==rchild:
                return lchild
            else:
                return root
        return _findParent(self.root,node1,node2)

    # 引申：如何计算二叉树中两个节点间的距离
    def getNodeDistance(self,node1,node2):
        parentNode=self.findComParent3(node1,node2)
        num1=self.getNodeNum(node1)
        level1=int(math.log(num1,2))
        num2=self.getNodeNum(node2)
        level2 = int(math.log(num2, 2))
        num3=self.getNodeNum(parentNode)
        level3 = int(math.log(num3, 2))

        return level1+level2-2*level3

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

    print(T1.findComParent2(node6,node8).x)
    print(T1.findComParent3(node7,node9).x)
    print(T1.getNodeDistance(node7,node6))