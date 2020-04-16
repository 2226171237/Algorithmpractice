# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回对应节点TreeNode
    def __init__(self):
        self.minNode=None

    def KthNode(self, pRoot, k):
        # write code here 中序遍历
        if pRoot == None or k <= 0:
            return None

        def _inorder(pRoot, k, r):
            if pRoot == None:
                return r
            m = _inorder(pRoot.left, k, r)
            m = m + 1
            if m == k:
                self.minNode = pRoot
                return m
            else:
                n = _inorder(pRoot.right, k, m)
                return n

        _inorder(pRoot, k, 0)
        return self.minNode

    def noReKthNode(self, pRoot, k):
        # 非递归实现
        if pRoot==None or k<=0:
            return None
        Stack=[pRoot]
        cnt=0
        while len(Stack):
            node=Stack[-1]
            while node:
                node=node.left
                Stack.append(node)
            Stack.pop()
            if len(Stack):
                node=Stack.pop()
                cnt+=1
                if cnt==k:
                    return node
                else:
                    Stack.append(node.right)




if __name__ == '__main__':
    root=TreeNode(5)
    root.left=TreeNode(3)
    root.right=TreeNode(7)
    root.left.left=TreeNode(2)
    root.left.right=TreeNode(4)
    root.right.left=TreeNode(6)
    root.right.right=TreeNode(8)
    S=Solution()
    print(S.noReKthNode(root,1).val)