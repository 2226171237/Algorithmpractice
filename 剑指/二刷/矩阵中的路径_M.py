'''
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
路径可以从矩阵中的任意一格开始，每一步可以在矩阵中向左、右、上、下移动一格。
如果一条路径经过了矩阵的某一格，那么该路径不能再次进入该格子。
例如，在下面的3×4的矩阵中包含一条字符串“bfce”的路径（路径中的字母用加粗标出）。

[["a","b","c","e"],
["s","f","c","s"],
["a","d","e","e"]]

但矩阵中不包含字符串“abfb”的路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子。

示例 1：
输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true

示例 2：
输入：board = [["a","b"],["c","d"]], word = "abcd"
输出：false
提示：
1 <= board.length <= 200
1 <= board[i].length <= 200

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ju-zhen-zhong-de-lu-jing-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        rows=len(board)
        if rows==0:
            return False
        cols=len(board[0])
        marked=[[False for _ in range(cols)] for _ in range(rows)]
        def isValid(i,j):
            return 0<=i<rows and 0<=j<cols and not marked[i][j]

        def dfs(i,j,word_i):
            if word_i==len(word):
                return True
            if not isValid(i,j):
                return False
            if board[i][j]==word[word_i]:
                marked[i][j] = True
                if dfs(i+1,j,word_i+1):
                    return True
                if dfs(i,j+1,word_i+1):
                    return True
                if dfs(i-1,j,word_i+1):
                    return True
                if dfs(i,j-1,word_i+1):
                    return True
                marked[i][j] = False
                return False
            else:
                return False

        for i in range(rows):
            for j in range(cols):
                if dfs(i,j,0):
                    return True
        return False

if __name__ == '__main__':
    s=Solution()
    print(s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCED"))