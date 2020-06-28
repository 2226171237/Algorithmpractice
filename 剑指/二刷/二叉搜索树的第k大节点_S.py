'''
给定一棵二叉搜索树，请找出其中第k大的节点。
'''
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def kthLargest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        cnt=[0]
        result=[0]
        def _inorder(root):
            if root==None or cnt[0]>k:
                return
            _inorder(root.right)
            cnt[0]+=1
            if cnt[0]==k:
                result[0]=root.val
                return
            _inorder(root.left)

        _inorder(root)
        return result[0]

if __name__ == '__main__':
    s=Solution()
    root=TreeNode(5)
    root.left=TreeNode(3)
    root.right=TreeNode(6)
    root.left.left=TreeNode(2)
    root.left.right=TreeNode(4)
    root.left.left.left=TreeNode(1)
    print(s.kthLargest(root,4))