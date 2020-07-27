'''
给定一个二叉树，判断其是否是一个有效的二叉搜索树。
假设一个二叉搜索树具有如下特征：
节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/validate-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        MINS=[float('-inf')]
        def inorder(root):
            if root==None:
                return True
            if not inorder(root.left):
                return False
            if root.val<=MINS[0]:
                return False
            MINS[0]=root.val
            return inorder(root.right)
        return inorder(root)


if __name__ == '__main__':
    s=Solution()
    root=TreeNode(1)
    root.left=TreeNode(1)
    print(s.isValidBST(root))