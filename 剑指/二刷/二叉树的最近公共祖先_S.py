'''
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，
最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-cha-shu-de-zui-jin-gong-gong-zu-xian-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        def dfs(root,p,path):
            if root==p:
                path.append(root)
                return True
            if root==None:
                return False
            A1=dfs(root.left,p,path)
            A2=dfs(root.right,p,path)
            if A1 or A2:
                path.append(root)
            return A1 or A2

        pPath=[]
        dfs(root,p,pPath)
        qPath=[]
        dfs(root,q,qPath)
        i=len(pPath)-1
        j=len(qPath)-1
        while i>=0 and j>=0:
            if pPath[i]!=qPath[j]:
                break
            i-=1
            j-=1
        return pPath[i+1]

    def lowestCommonAncestor2(self, root, p, q):
        if None==root:
            return None
        if root==p or root==q:
            return root
        A1=self.lowestCommonAncestor2(root.left,p,q)
        A2=self.lowestCommonAncestor2(root.right,p,q)
        if A1 and A2:
            return root
        return A1 if A1 else A2

if __name__ == '__main__':
    s=Solution()





