
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def countPairs(self, root, distance):
        """
        :type root: TreeNode
        :type distance: int
        :rtype: int
        """
        if root==None:
            return 0

        cnt=[0]
        def find(root,distance): # 返回叶节点到根节点的距离
            if root==None:
                return []
            if root.left==None and root.right==None:
                return [0]
            left=find(root.left,distance)
            right=find(root.right,distance)
            for x in left:
                for y in right:
                    if x+y+2<=distance:
                        cnt[0]+=1
            res=[x+1 for x in left+right]
            return res
        return cnt[0]


if __name__ == '__main__':
    root=TreeNode(1)
    root.left=TreeNode(2)
    root.right=TreeNode(3)
    root.left.right=TreeNode(4)
    s=Solution()
    print(s.countPairs(root,3))




