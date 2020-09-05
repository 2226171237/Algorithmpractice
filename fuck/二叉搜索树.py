

class TreeNode:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

def isSumTree(root1,root2):
    '''判断两颗树是否相等'''
    if root1==None and root2==None:
        return True
    if root1==None or root2==None:
        return False
    if root1.val!=root2.val:
        return False
    return isSumTree(root1.left,root2.left) and isSumTree(root1.right,root2.right)


def isValidBST(root):
    '''判断 BST 的合法性'''
    leftMins=float('-inf')
    def inOrder(root):      # 中序遍历
        nonlocal leftMins
        if None==root:
            return True
        if not inOrder(root.left):
            return False
        if not leftMins<=root.val:
            return False
        leftMins=root.val
        return inOrder(root.right)
    return inOrder(root)

#        3
#       / \
#      2   4
#     / \
#    0   5
root=TreeNode(3)
root.left=TreeNode(2)
root.right=TreeNode(4)
root.left.left=TreeNode(0)
root.left.right=TreeNode(5)
print(isValidBST(root))  # Fasle

##在 BST 中查找一个数是否存在**
def isInBST(root,target):
    if None==root:
        return False
    if root.val==target:
        return True
    if target<root.val:
        return isInBST(root.left,target)
    else:
        return isInBST(root.right,target)
root.left.right.val=2.5
print(isInBST(root,6))


#  在 BST 中插入一个数
def insertToBST(root,val):
    if None==root:
        return TreeNode(val)
    if val<root.val:
        root.left=insertToBST(root.left,val)
    else:
        root.right=insertToBST(root.right,val)
    return root
insertToBST(root,2.4)
insertToBST(root,3.5)

# 在 BST 中删除一个数

def getMins(root):
    if root==None:
        return None
    node=root
    while node.left:
        node=node.left
    return node
def deleteBST(root,val):
    if None==root:
        return None
    if val<root.val:
        root.left=deleteBST(root.left,val)
    elif val==root.val:
        if root.left==None and root.right==None:
            return None
        else:
            min_node=getMins(root.right)
            if min_node==None:
                root.val=root.left.val
                root.left=deleteBST(root.left,root.val)
            else:
                root.val=min_node.val
                root.right=deleteBST(root.right,root.val)
            return root
    else:
        root.right=deleteBST(root.right,val)
    return root

root=deleteBST(root,4)
print('ok')
