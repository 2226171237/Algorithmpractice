'''
输入一棵二叉树的根节点，判断该树是不是平衡二叉树。如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。
示例 1:
给定二叉树 [3,9,20,null,null,15,7]

    3
   / \
  9  20
    /  \
   15   7
返回 true 。
示例 2:
给定二叉树 [1,2,2,3,3,null,null,4,4]
       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
返回 false 。

限制：
1 <= 树的结点个数 <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ping-heng-er-cha-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def treeDepth(self,root):
        if None==root:
            return 0
        return max(self.treeDepth(root.left),self.treeDepth(root.right))+1

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def _isbalanced(root):
            if None==root:
                return True,0
            A,h1=_isbalanced(root.left)
            if A==False:
                return False,h1
            B,h2=_isbalanced(root.right)
            if B==False:
                return False,h2
            if abs(h1-h2)<=1:
                return True,max(h1,h2)+1
            else:
                return False,max(h1,h2)+1

        A=_isbalanced(root)
        return A
    