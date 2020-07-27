'''
请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，
第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：
[
  [3],
  [20,9],
  [15,7]
]
提示：
节点总数 <= 1000
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# Definition for a binary tree node.
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
        if None==root:
            return []
        result=[]
        Q=deque()
        Q.append((root))
        flipFlag=False
        while len(Q):
            tmp=[]
            cur_size=len(Q)
            for _ in range(cur_size):
                node=Q.popleft()
                tmp.append(node.val)
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
            result.append(tmp[::-1] if flipFlag else tmp)
            flipFlag=not flipFlag
        return result
