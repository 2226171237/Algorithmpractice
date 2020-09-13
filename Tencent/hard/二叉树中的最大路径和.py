'''
给定一个非空二叉树，返回其最大路径和。
本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。
示例 1:
输入: [1,2,3]

       1
      / \
     2   3
输出: 6
示例 2:
输入: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7
输出: 42

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-maximum-path-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        resMax=[-2**31]

        def midOrder(root): # 到根节点的最大路径
            if root==None:
                return -2**31
            leftmax=midOrder(root.left)
            rightmax=midOrder(root.right)
            resMax[0]=max(resMax[0],leftmax,rightmax,leftmax+root.val,rightmax+root.val,leftmax+rightmax+root.val,root.val)
            return max(root.val,root.val+leftmax,root.val+rightmax)

        t=midOrder(root)
        return max(t,resMax[0])

if __name__ == '__main__':
    root=TreeNode(-3)
    s=Solution()
    print(s.maxPathSum(root))

