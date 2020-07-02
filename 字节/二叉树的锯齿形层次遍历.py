'''
给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

例如：
给定二叉树 [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
返回锯齿形层次遍历如下：
[ [3],
  [20,9],
  [15,7]]
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if None==root:
            return []
        res=[]

        Q=deque()
        Q.append(root)
        flip=True

        while len(Q):
            cur_layer=[]
            cur_len=len(Q)
            for _ in range(cur_len):
                root=Q.popleft()
                cur_layer.append(root.val)
                if root.left:
                    Q.append(root.left)
                if root.right:
                    Q.append(root.right)
            if flip:
                res.append(cur_layer)
            else:
                res.append(cur_layer[::-1])
            flip=not flip
        return res

