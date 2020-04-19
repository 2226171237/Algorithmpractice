'''
给定一个二叉树，检查它是否是镜像对称的。
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        '''
        用递归
        :param root:
        :return:
        '''
        def _isSymmetric(root1:TreeNode,root2:TreeNode)->bool:
            if root1==root2==None:
                return True
            if root1==None or root2==None:
                return False
            return root1.val==root2.val and _isSymmetric(root1.left,root2.right) and _isSymmetric(root1.right,root2.left)
        return _isSymmetric(root.left,root.right)



if __name__ == '__main__':
    S=Solution()
    root=TreeNode(1)
    root.left=TreeNode(2)
    root.right=TreeNode(2)
    root.left.left=TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left=TreeNode(4)
    root.right.right=TreeNode(3)
    print(S.isSymmetric(root))
