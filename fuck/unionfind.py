

class UF:
    def __init__(self,N):
        self.ids=list(range(N))
        self._counts=N

    def union(self,p,q):
        pRoot=self.find(p)
        qRoot=self.find(q)
        if pRoot==qRoot:
            return
        self.ids[qRoot]=pRoot
        self._counts-=1

    def find(self,p):
        while self.ids[p]!=p:
            p=self.ids[p]
        return p

    def connect(self,p,q):
        pRoot=self.find(p)
        qRoot=self.find(q)
        return pRoot==qRoot

    def __len__(self):
        return self._counts


# 130. 被围绕的区域
class Solution(object):
    def solve1(self, board):
        """
        方法1： DFS
        对四个边进行dfs遍历O，找到和边界O相连的O，修改为 "#", 全部遍历完后，没有修改的O就改为X，#改为O
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        m,n=len(board),len(board[0])
        def isValid(i,j):
            return 0<=i<m and 0<=j<n and board[i][j]=='O'

        def dfs(i,j):
            if not isValid(i,j):
                return
            board[i][j]='#'
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        for i in range(m):
            for j in range(n):
                if not(1<=i<m-1 and 1<=j<n-1):
                    dfs(i,j)
        for i in range(m):
            for j in range(n):
                if board[i][j]=='O':
                    board[i][j]='X'
                elif board[i][j]=='#':
                    board[i][j]='O'

boards=[['X', 'X', 'X', 'X', 'O'],
        ['X', 'X', 'X', 'O', 'X'],
        ['O', 'O', 'X', 'O', 'X'],
        ['X', 'O', 'X', 'X', 'X']]
s=Solution()
s.solve1(boards)
for b in boards:
    print(b)


# 给你一个数组equations，装着若干字符串表示的算式。每个算式equations[i]长度都是 4，
# 而且只有这两种情况：a==b或者a!=b，其中a,b可以是任意小写字母。
# 你写一个算法，如果equations中所有算式都不会互相冲突，返回 true，否则返回 false。
#
# 比如说，输入["a==b","b!=c","c==a"]，算法返回 false，因为这三个算式不可能同时正确。
#
# 再比如，输入["c==c","b==d","x!=z"]，算法返回 true，因为这三个算式并不会造成逻辑冲突。

def isValidEqu(equations):
    uf=UF(3)
    notequs=[]
    for eq in equations:
        a = ord(eq[0]) - ord('a')
        b = ord(eq[-1]) - ord('a')
        if eq[1]=='=':
            uf.union(a,b)
        else:
            notequs.append((a,b))
    for a,b in notequs:
        if uf.connect(a,b):
            return False
    return True

print(isValidEqu(['a==b','b!=c','c==a']))
