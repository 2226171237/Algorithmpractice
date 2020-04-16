'''
线索二叉树
'''
# 以该节点构成的二叉树为线索二叉树。
class BNode:
    def __init__(self,x,lchild=None,rchild=None,LTag=False,RTag=False):
        # 带有前驱和后继标志
        # 当LTag=False,则lchild为左子树，否则表名是前驱，同理RTag
        self.x=x
        self.lchild=lchild
        self.rchild=rchild
        self.LTag=LTag
        self.RTag=RTag


class BiThrTree:
    def __init__(self):
        self.head=BNode(None)
        self.head.LTag=False
        self.head.RTag=True

    def is_empty(self):
        return self.head.lchild ==None


    def inOrderTraverse(self,visit_fn):
        root=self.head.lchild
        while root!=self.head:
            while not root.LTag: # 向下走
                root=root.lchild
            visit_fn(root)
            while root.RTag and root.rchild!=self.head: # 访问后继
                root=root.rchild # 后继
                visit_fn(root)
            root=root.rchild

    def array2tree(self,arr):
        '''
        先序序列转二叉树
        :param arr:
        :return:
        '''
        def _createBinTree(arr,i):
            if i<len(arr) and arr[i]!=' ':
                root=BNode(arr[i])
                root.lchild,i=_createBinTree(arr,i+1)
                root.rchild,i=_createBinTree(arr,i+1)
            else:
                root=None
            return root,i
        self.head.lchild,_=_createBinTree(arr,0)

    def reInOrderTraverse(self,root,visit_fn):
        '''
        中序遍历，递归实现
        :param root: 根节点
        :param visit_fn: 处理函数
        :return:
        '''
        if None==root:
            return
        self.reInOrderTraverse(root.lchild,visit_fn)
        visit_fn(root)
        self.reInOrderTraverse(root.rchild,visit_fn)

    def inOrderThreading(self):
        '''
        中序遍历二叉树，并将其线索化
        :return:
        '''
        def _inThreading(root,pred):
            if root==None or root==self.head:
                return pred
            pred=_inThreading(root.lchild,pred)
            if root.lchild ==None:
                root.LTag=True
                root.lchild=pred
            if pred.rchild==None:
                pred.RTag=True
                pred.rchild=root
            pred=root
            pred=_inThreading(root.rchild,pred)
            return pred

        pred=_inThreading(self.head.lchild,self.head)
        pred.rchild=self.head
        self.head.rchild=pred

if __name__ == '__main__':

    def printf(node):
        print(node.x,end=' ')

    T=BiThrTree()

    node1=BNode('1')
    node2=BNode('2')
    node3=BNode('3')
    node4=BNode('4')
    node5=BNode('5')
    node6=BNode('6')
    node7=BNode('7')
    node8=BNode('8')
    node9=BNode('9')
    node10=BNode('10')
    node11=BNode('11')
    T.head.lchild=node1
    node1.lchild=node2
    node1.rchild=node3
    node3.lchild=node4
    node3.rchild=node5
    node4.lchild=node6
    node4.rchild=node7
    node5.lchild = node10
    node6.rchild = node11
    node7.lchild=node8
    node7.rchild=node9
    T.reInOrderTraverse(T.head.lchild, printf)

    # 线索化
    # node2.LTag=True
    # node2.RTag=True
    # node2.lchild=T.head
    # node2.rchild=node1
    # node6.LTag=True
    # node6.lchild=node1
    # node11.RTag=True
    # node11.LTag=True
    # node11.lchild=node6
    # node11.rchild=node4
    # node8.LTag=True
    # node8.RTag=True
    # node8.lchild=node4
    # node8.rchild=node7
    # node9.LTag=True
    # node9.RTag=True
    # node9.lchild=node7
    # node9.rchild=node3
    # node10.RTag=True
    # node10.LTag=True
    # node10.lchild=node3
    # node10.rchild=node5
    # node5.RTag = True
    # node5.rchild=T.head

    print()
    T.inOrderThreading()
    T.inOrderTraverse(printf)






