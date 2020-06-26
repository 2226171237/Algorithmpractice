'''
输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder)==0:
            return None
        head=TreeNode(preorder[0])
        i=0
        while i<len(inorder):
            if inorder[i]==preorder[0]:
                break
            else:
                i+=1
        head.left=self.buildTree(preorder[1:i+1],inorder[:i])
        head.right=self.buildTree(preorder[i+1:],inorder[i+1:])
        return head

if __name__ == '__main__':
    s=Solution()
    head=s.buildTree([3,9,20,15,7],[9,3,15,20,7])
    print(12)
