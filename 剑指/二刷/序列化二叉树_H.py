'''
请实现两个函数，分别用来序列化和反序列化二叉树。
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque
class Codec:

    def serialize1(self,root):
        '''前序遍历序列化'''
        if None==root:
            return '[null]'
        s='['
        def _preOrder(root):
            nonlocal s
            if None==root:
                s+='null,'
                return
            s+=str(root.val)+','
            _preOrder(root.left)
            _preOrder(root.right)
        _preOrder(root)
        s=s[:-1]+']'
        return s

    def deserialize1(self,data):
        '''前序反序列化'''
        data=data[1:-1].split(',')
        data=[int(v) if v!='null' else None for v in data]

        count=[0]
        def _inorder(data):
            if count[0]>=len(data):
                return None
            if data[count[0]]==None:
                count[0] += 1
                return None
            root=TreeNode(data[count[0]])
            count[0]+=1
            root.left=_inorder(data)
            root.right=_inorder(data)
            return root

        root=_inorder(data)
        return root

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if None==root:
            return '[null]'
        Q=deque()
        Q.append(root)
        s='['
        while len(Q):
            root=Q.popleft()
            if root==None:
                s+='null,'
            else:
                s+=str(root.val)+','
                Q.append(root.left)
                Q.append(root.right)
        s=s[:-1]+']'
        return s

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data=data[1:-1].split(',')
        data=[int(x) if x!='null' else None for x in data]
        if data[0]==None:
            return None
        Q=deque()
        root=TreeNode(data[0])
        Q.append(root)
        i=1
        while len(Q):
            node=Q.popleft()
            if data[i]:
                node.left=TreeNode(data[i])
                Q.append(node.left)
            i=i+1
            if data[i]:
                node.right=TreeNode(data[i])
                Q.append(node.right)
            i+=1
        return root




# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))


if __name__ == '__main__':
    codec=Codec()
    root=TreeNode(5)
    root.left=TreeNode(2)
    root.right=TreeNode(3)
    root.right.left=TreeNode(2)
    root.right.right=TreeNode(4)
    root.right.left.left=TreeNode(3)
    root.right.left.right=TreeNode(1)
    data=codec.serialize1(root)
    print(data)
    root=codec.deserialize1(data)
    data=codec.serialize1(root)
    print(data)
    data=codec.serialize(root)
    print(data)
    root=codec.deserialize(data)
    data=codec.serialize(root)
    print(data)