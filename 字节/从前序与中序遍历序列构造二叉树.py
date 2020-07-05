'''
根据一棵树的前序遍历与中序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。
例如，给出
前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：
    3
   / \
  9  20
    /  \
   15   7
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
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
        root=TreeNode(preorder[0])
        k=0
        for i in range(len(inorder)):
            if inorder[i]==preorder[0]:
                k=i
                break
        root.left=self.buildTree(preorder[1:k+1],inorder[:k])
        root.right=self.buildTree(preorder[k+1:],inorder[k+1:])
        return root

if __name__ == '__main__':
    s=Solution()
    s.buildTree([3,9,20,15,7],[9,3,15,20,7])
