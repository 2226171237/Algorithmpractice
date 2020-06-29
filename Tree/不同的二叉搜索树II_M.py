'''
leetcode 95: 给定一个整数 n，生成所有由 1 ... n 为节点所组成的 二叉搜索树 。
'''
# Definition for a binary tree node.
import copy
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        result=[]

        def dfs(root,path,visited):
            if len(path)==n:
                result.append(copy.deepcopy(root))
                return
            for i in range(1,n+1):
                if visited[i-1]==False:
                    visited[i-1]=True
                    path.append(i)
                    newnode,parent=self.insert_node(root,i)
                    if root==None:
                        root=newnode
                    dfs(root,path,visited)
                    if parent==None:
                        root=None
                    else:
                        if parent.left==newnode:
                            parent.left=None
                        else:
                            parent.right=None
                    path.pop()
                    visited[i-1]=False

        dfs(None,[],[False for _ in range(n)])
        return result

    def insert_node(self,root,x):
        if root==None:
            return TreeNode(x),root
        node=root
        parent=node
        while node:
            parent = node
            if node.val>x:
                node=node.left
            else:
                node=node.right
        newnode=TreeNode(x)
        if parent.val>x:
            parent.left=newnode
        else:
            parent.right=newnode

        return newnode,parent

if __name__ == '__main__':
    S=Solution()
    result=S.generateTrees(3)
    print()

