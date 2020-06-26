'''
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。
要求不能创建任何新的节点，只能调整树中节点指针的指向。
'''

# Definition for a Node.
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def __init__(self):
        self.pHead=None
        self.pEnd=None
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root==None:
            return None

        def dfs(root):
            '''中序遍历'''
            if root == None:
                return None
            dfs(root.left)
            root.left=self.pEnd
            if None==self.pEnd:
                self.pHead=root
            else:
                self.pEnd.right=root
            self.pEnd=root
            dfs(root.right)
        dfs(root)
        self.pHead.left=self.pEnd
        self.pEnd.right=self.pHead
        return self.pHead


if __name__ == '__main__':
    s=Solution()
    root=Node(4)
    root.left=Node(2)
    root.right=Node(5)
    root.left.left=Node(1)
    root.left.right=Node(3)
    head=s.treeToDoublyList(root)
    print(head)




