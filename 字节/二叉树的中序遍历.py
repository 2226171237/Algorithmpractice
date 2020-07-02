'''
给定一个二叉树，返回它的中序 遍历。
示例:
输入: [1,null,2,3]
   1
    \
     2
    /
   3
输出: [1,3,2]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-inorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        递归
        :type root: TreeNode
        :rtype: List[int]
        """
        res=[]

        def inorder(root):
            if None==root:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)

        inorder(root)
        return res

    def inorderTraversal2(self,root):
        '''非递归'''
        if None==root:
            return []
        stack=[root]
        res=[]
        while len(stack):
            node=stack[-1]
            if node==None:
                stack.pop()
                if len(stack):
                    node=stack.pop()
                    res.append(node.val)
                    stack.append(node.right)
            else:
                node=node.left
                stack.append(node)
        return res

if __name__ == '__main__':
    s=Solution()
    root=TreeNode(1)
    root.left=TreeNode(2)
    root.right=TreeNode(3)
    root.left.left=TreeNode(4)
    root.left.right=TreeNode(5)
    root.left.right.left=TreeNode(6)
    root.right.left=TreeNode(7)
    root.right.left.right=TreeNode(8)
    print(s.inorderTraversal2(root))
    print(s.inorderTraversal(root))
