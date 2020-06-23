'''
输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。
从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。

提示：
节点总数 <= 10000
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        result=[]
        def dfs(root,sum,path):
            if root==None: # 对于那些单子结点，可能会进入None
                return
            if root.left==None and root.right==None:  # 到叶节点结束
                if sum==root.val:
                    path.append(root.val)
                    result.append(path.copy())
                    path.pop()
                return
            path.append(root.val)
            dfs(root.left,sum-root.val,path)
            dfs(root.right,sum-root.val,path)
            path.pop()

        dfs(root,sum,[])
        return result

if __name__ == '__main__':
    s=Solution()
    root=TreeNode(5)
    root.left=TreeNode(4)
    root.right=TreeNode(8)
    root.left.left=TreeNode(11)
    root.left.left.left=TreeNode(7)
    root.left.left.right=TreeNode(2)
    root.right.left=TreeNode(13)
    root.right.right=TreeNode(4)
    root.right.right.left=TreeNode(5)
    root.right.right.right=TreeNode(1)
    print(s.pathSum(root,22))