
# leetcode 111 :给定一个二叉树，找到其最小深度。
class TreeNode:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

from collections import deque
def getMinDepth(root):
    if None==root:
        return 0
    Q=deque()
    Q.append(root)
    depth=1
    while len(Q):
        sz=len(Q)
        for _ in range(sz):
            node=Q.popleft()
            if node.left==None and node.right==None:
                return depth
            if node.left:
                Q.append(node.left)
            if node.right:
                Q.append(node.right)
        depth+=1
    return depth

root=TreeNode(3)
root.left=TreeNode(9)
root.right=TreeNode(20)
root.right.left=TreeNode(15)
root.right.right=TreeNode(7)
print(getMinDepth(root))

# leetcode 752: 打开旋转锁，
class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        result=set()
        deadends=set(deadends)
        def bfs(passwd):
            Q=deque()
            Q.append(passwd[:])
            times=0
            while len(Q):
                sz=len(Q)
                for _ in range(sz):
                    passwd=Q.popleft()
                    passwd_str=''.join(map(str,passwd))
                    if passwd_str==target:
                        return times
                    if passwd_str in result or passwd_str in deadends:
                        continue
                    result.add(passwd_str)
                    for i in range(4):  # 共8种拨法，8叉树
                        t=passwd[i]
                        passwd[i]+=1
                        if passwd[i]<=9:
                            Q.append(passwd[:])   # 往上拨
                        passwd[i]=9 if t-1==-1 else t-1
                        if passwd[i]>=0:
                            Q.append(passwd[:])   # 往下拨
                        passwd[i]=t
                times+=1
            return -1
        t=bfs([0,0,0,0])
        return t

s=Solution()
print(s.openLock(["8888"],'9999'))
