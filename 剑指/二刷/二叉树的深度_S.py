'''
输入一棵二叉树的根节点，求该树的深度。
从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径，最长路径的长度为树的深度。
提示：
节点总数 <= 10000
'''
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if None==root:
            return 0
        return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))

if __name__ == '__main__':
    s=Solution()
    root=TreeNode(1)
    root.right=TreeNode(2)
    print(s.maxDepth(root))