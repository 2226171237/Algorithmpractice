

# 判断 BST 的合法性
class TreeNode:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

def isValidBST(root):
    def _isvalid(root,mins,maxs):
        if None==root:
            return True
        left=mins.val if mins else float('-inf')
        right=maxs.val if maxs else float('inf')
        if not left<=root.val<=right:
            return False
        return _isvalid(root.left,mins,root) and _isvalid(root.right,root,maxs)
    return _isvalid(root,None,None)

def search(root,target):
    if None==root:
        return False
    if root.val==target:
        return True
    if root.val<target:
        return search(root.right,target)
    if root.val>target:
        return search(root.left,target)

def insert(root,x):
    '''插入一个结点，并返回这个树的根'''
    if None==root:
        return TreeNode(x)
    if root.val<x:
        root.right=insert(root.right,x) # 在右子树插入得到新的右子树
    if root.val>x:
        root.left=insert(root.left,x)  # 在左子树叉树，得到新的左子树
    return root


def getMin(root):
    if root==None:
        return None
    node=root
    while node.left:
        node=node.left
    return node

def delBST(root,val):
    '''删除一个结点，并返回这个树的根'''
    if None==root:
        return None
    if root.val==val:
        # 最多有一个子结点
        if root.left==None:
            return root.right
        if root.right==None:
            return root.left
        # 有两个子结点
        # 找到右子树的最小结点和当前结点替换，并删除最小结点
        node=getMin(root.right)
        root.val=node.val
        root.right=delBST(root.right,node.val)
    if root.val>val:
        root.left=delBST(root.left,val)  # 在右子树删除得到新的右子树
    if root.val<val:
        root.right=delBST(root.right,val) # 在左子树删除，得到新的左子树
    return root









