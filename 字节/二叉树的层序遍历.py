'''
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。

示例：
二叉树：[3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：
[  [3],
  [9,20],
  [15,7]]
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-level-order-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
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
        if None==root:
            return []

        res=[]
        h_set=set()
        Q=deque()
        Q.append((root,0))
        while len(Q):
            root,h=Q.popleft()
            if h not in h_set:
                h_set.add(h)
                res.append([root.val])
            else:
                res[h].append(root.val)
            if root.left:
                Q.append((root.left,h+1))
            if root.right:
                Q.append((root.right,h+1))

        return res

    def levelOrder2(self, root):
        if None==root:
            return []
        res=[]
        Q=deque()
        Q.append(root)
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
            res.append(cur_layer)
        return res

if __name__ == '__main__':
    s=Solution()
    root=TreeNode(1)
    root.left=TreeNode(2)
    root.right=TreeNode(3)
    root.right.left=TreeNode(4)
    root.right.right=TreeNode(5)
    print(s.levelOrder(root))
    print(s.levelOrder2(root))