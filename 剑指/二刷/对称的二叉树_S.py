'''
请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
    1
   / \
  2   2
   \   \
   3    3
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/dui-cheng-de-er-cha-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def _isSymmetric(root1,root2):
            if None==root1 and None==root2:
                return True
            if None==root1:
                return False
            if None==root2:
                return False
            if root1.val!=root2.val:
                return False
            A=_isSymmetric(root1.left,root2.right)
            if not A:
                return False
            B=_isSymmetric(root1.right,root2.left)
            return A and B

        return _isSymmetric(root,root)