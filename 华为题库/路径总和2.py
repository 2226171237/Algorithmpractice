'''
给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。
说明: 叶子节点是指没有子节点的节点。
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int):
        '''

        :param root:
        :param sum:
        :return:
        '''
        result=[]
        def dfs(root:TreeNode,sum:int,path:list):
            if root==None:
                return
            if root.left==None and root.right==None:
                if sum==root.val:
                    path.append(root.val)
                    result.append(path[:])
                    path.pop()
                return
            path.append(root.val)
            if root.left:
                dfs(root.left,sum-root.val,path)
            if root.right:
                dfs(root.right,sum-root.val,path)
            path.pop()

        dfs(root,sum,[])
        return result

if __name__ == '__main__':
    S=Solution()
    root=TreeNode(5)
    root.left=TreeNode(4)
    root.right=TreeNode(8)
    root.left.left=TreeNode(11)
    root.right.left=TreeNode(13)
    root.right.right=TreeNode(4)
    root.left.left.left=TreeNode(7)
    root.left.left.right=TreeNode(2)
    root.right.right.left=TreeNode(5)
    root.right.right.right=TreeNode(1)

    print(S.pathSum(root,22))