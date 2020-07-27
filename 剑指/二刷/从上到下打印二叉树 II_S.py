'''
从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。
'''
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result=[]
        if None==root:
            return result

        Q=deque()
        Q.append(root)
        while len(Q):
            tmp=[]
            size=len(Q)
            for _ in range(size):
                node=Q.popleft()
                tmp.append(node.val)
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
            result.append(tmp)
        return result
