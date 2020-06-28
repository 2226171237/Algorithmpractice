'''
输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)
B是A的子结构， 即 A中有出现和B相同的结构和节点值。
'''
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def scanSubTree(self,A,B):
        if None==B:
            return True
        if A==None and B!=None:
            return False
        if A.val==B.val:
            left=self.scanSubTree(A.left,B.left)
            right=self.scanSubTree(A.right,B.right)
            return left and right
        else:
            return False

    def isSubStructure(self, A, B):
        """
        :type A: TreeNode
        :type B: TreeNode
        :rtype: bool
        """
        if None==A or B==None:
            return False
        if A.val==B.val:
            if self.scanSubTree(A,B):
                return True
        return  self.isSubStructure(A.left,B) or self.isSubStructure(A.right,B)

if __name__ == '__main__':
    s=Solution()
    A=TreeNode(3)
    A.left=TreeNode(4)
    A.right=TreeNode(5)
    A.left.left=TreeNode(1)
    A.left.right=TreeNode(2)
    A.left.right.left=TreeNode(6)
    A.left.right.right=TreeNode(7)
    A.right.left=TreeNode(9)
    A.right.right=TreeNode(10)

    B=TreeNode(4)
    B.right=TreeNode(2)
    B.right.left=TreeNode(6)

    print(s.isSubStructure(A,B))
