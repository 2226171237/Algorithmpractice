'''
给定一个二叉搜索树，编写一个函数 kthSmallest 来查找其中第 k 个最小的元素。
说明：
你可以假设 k 总是有效的，1 ≤ k ≤ 二叉搜索树元素个数。

示例 1:
输入: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
输出: 1
示例 2:
输入: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
输出: 3
进阶：
如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 k 小的值，你将如何优化 kthSmallest 函数？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/kth-smallest-element-in-a-bst
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def __init__(self):
        self.cnt=0
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        res=[0]
        def midOrder(root):
            if root==None:
                return
            midOrder(root.left)
            self.cnt+=1
            if self.cnt==k:
                res[0]=root.val
                return
            else:
                midOrder(root.right)
        midOrder(root)
        return res[0]


if __name__ == '__main__':
    root=TreeNode(5)
    root.left=TreeNode(3)
    root.right=TreeNode(6)
    root.left.left=TreeNode(2)
    root.left.right=TreeNode(4)
    root.left.left.left=TreeNode(1)
    s=Solution()
    print(s.kthSmallest(root,3))
