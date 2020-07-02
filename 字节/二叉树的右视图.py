'''
给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

示例:
输入: [1,2,3,null,5,null,4]
输出: [1, 3, 4]
解释:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-right-side-view
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque

class Solution(object):
    def rightSideView(self, root):
        """
        每层最右边结点
        :type root: TreeNode
        :rtype: List[int]
        """
        if None==root:
            return []

        res=[]
        Q=deque()
        Q.append((root,0))
        while len(Q):
            node,h=Q.popleft()
            if len(Q)==0 or Q[0][-1]!=h:
                res.append(node.val)
            if node.left:
                Q.append((node.left,h+1))
            if node.right:
                Q.append((node.right,h+1))
        return res

if __name__ == '__main__':
    s=Solution()
    root=TreeNode(1)
    root.left=TreeNode(2)
    root.right=TreeNode(3)
    root.right.left=TreeNode(5)
    print(s.rightSideView(root))



