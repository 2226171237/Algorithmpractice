'''
leetcode 156
给定一个二叉树，其中所有的右节点要么是具有兄弟节点（拥有相同父节点的左节点）的叶节点，要么为空，将此二叉树上下翻转并将它变成一棵树，
原来的右节点将转换成左叶节点。返回新的根。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-upside-down
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
        '''
        假设：已经知道如何对root的左子树进行上下翻转。
        则，root的右子树要添加到翻转子树的最右叶节点的左边，root添加到右边。
        :param root:
        :return:
        '''
        if root==None:
            return None
        if root.left==None and root.right==None:
            return root
        new_root=self.upsideDownBinaryTree(root.left)
        node=new_root
        while node.right:
            node=node.right
        node.left=root.right
        node.right=TreeNode(root.val)
        return new_root


if __name__ == '__main__':
    root=TreeNode(1)
    root.left=TreeNode(2)
    root.right=TreeNode(3)
    root.left.left=TreeNode(4)
    root.left.right=TreeNode(5)
    S=Solution()
    new_root=S.upsideDownBinaryTree(root)
    print(new_root.val)



