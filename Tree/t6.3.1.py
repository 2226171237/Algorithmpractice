'''
遍历二叉树
'''
class BNode:
    def __init__(self,data,lchild=None,rchild=None):
        self.data=data
        self.lchild=lchild
        self.rchild=rchild

class Stack:
    def __init__(self):
        self.items=[]

    def is_empty(self):
        return len(self.items)==0

    def push(self,x):
        self.items.append(x)

    def pop(self):
        if self.is_empty():
            raise ValueError('stack is empty!')
        else:
            self.items.pop()
    def peek(self):
        if self.is_empty():
            raise ValueError('stack is empty!')
        else:
            return self.items[-1]

class BinTree:
    def __init__(self):
        self.root=None

    def is_empty(self):
        return self.root == None

    def arrat2tree(self,arr):

        def addNode(arr,low,high):
            if low>high:
                return None
            mid=(low+high)//2
            root=BNode(arr[mid])
            root.lchild=addNode(arr,low,mid-1)
            root.rchild=addNode(arr,mid+1,high)
            return root

        self.root=addNode(arr,0,len(arr)-1)

    def rePreOrderTraverse(self,root,visit_fn):
        '''
        先序遍历，递归实现
        :param root: 数的根节点
        :param visit_fn: 处理函数
        :return:
        '''
        if None==root:
            return
        visit_fn(root)
        self.rePreOrderTraverse(root.lchild,visit_fn)
        self.rePreOrderTraverse(root.rchild,visit_fn)

    def preOrderTraverse(self,visit_fn):
        '''
        先序遍历，非递归实现
        :return:
        '''
        S=Stack()
        S.push(self.root)
        while not S.is_empty():
            node=S.peek()
            S.pop()
            visit_fn(node)
            if node.rchild:
                S.push(node.rchild)
            if node.lchild:
                S.push(node.lchild)
        print()

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

    def inOrderTraverse(self,visit_fn):
        '''
        中序遍历，非递归实现
        :param visit_fn:
        :return:
        '''
        S=Stack()
        S.push(self.root)
        while not S.is_empty():
            top=S.peek()
            while top:
                S.push(top.lchild)
                top=S.peek()
            S.pop()
            if not S.is_empty():
                top=S.peek()
                S.pop()
                visit_fn(top)
                S.push(top.rchild)
        print()

    def reAfterOrderTraverse(self,root,visit_fn):
        '''
        后序遍历 递归实现
        :param root:
        :param visit_fn:
        :return:
        '''
        if root== None:
            return
        self.reAfterOrderTraverse(root.lchild,visit_fn)
        self.reAfterOrderTraverse(root.rchild,visit_fn)
        visit_fn(root)

    def afterOrderTraverse(self,visit_fn):
        '''
        后序遍历，非递归实现
        '''
        S=Stack()
        S.push(self.root)
        flags=set()
        i=0
        while not S.is_empty():
            top=S.peek()
            isPush=False
            if top.rchild and top.rchild not in flags:
                S.push(top.rchild)
                isPush=True
            if top.lchild and top.lchild not in flags:
                S.push(top.lchild)
                isPush=True
            if not isPush:
                visit_fn(top)
                S.pop()
                flags.add(top)

    def createBiTree(self,arr):
        '''
        根据先序序列创建二叉树
        :return:
        '''
        def _createBiTree(arr,i):
            if i<len(arr) and arr[i]!=' ':
                root=BNode(arr[i])
                root.lchild,i=_createBiTree(arr,i+1)
                root.rchild,i=_createBiTree(arr,i+1)
            else:
                root=None
            return root,i
        self.root,_=_createBiTree(arr,0)

if __name__ == '__main__':
    s='-+/a*efb-cd'
    T=BinTree()
    T.arrat2tree(s)

    def visit_fn(node):
        print(node.data,end=' ')

    T.rePreOrderTraverse(T.root,visit_fn)
    print()
    T.preOrderTraverse(visit_fn)

    T.reInOrderTraverse(T.root, visit_fn)
    print()
    T.inOrderTraverse(visit_fn)


    T.reAfterOrderTraverse(T.root,visit_fn)
    print()
    T.afterOrderTraverse(visit_fn)


    arr='ABC  DE G  F   '
    T.createBiTree(arr)
    print()
    T.rePreOrderTraverse(T.root,visit_fn)

