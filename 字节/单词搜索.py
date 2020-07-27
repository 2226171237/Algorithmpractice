'''
给定一个二维网格和一个单词，找出该单词是否存在于网格中。
单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。
同一个单元格内的字母不允许被重复使用。

示例:
board =[['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']]
给定 word = "ABCCED", 返回 true
给定 word = "SEE", 返回 true
给定 word = "ABCB", 返回 false
 
提示：
board 和 word 中只包含大写和小写英文字母。
1 <= board.length <= 200
1 <= board[i].length <= 200
1 <= word.length <= 10^3
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-search
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        rows,cols=len(board),len(board[0])

        marked=[[False for _ in range(cols)] for _ in range(rows)]

        def isValid(i,j):
            return 0<=i<rows and 0<=j<cols and marked[i][j]==False

        def dfs(board,i,j,k):
            if k==len(word):
                return True
            if not isValid(i,j):
                return False
            if board[i][j]==word[k]:
                marked[i][j]=True
                if dfs(board,i+1,j,k+1):
                    marked[i][j] = False
                    return True
                if dfs(board,i,j+1,k+1):
                    marked[i][j] = False
                    return True
                if dfs(board,i-1,j,k+1):
                    marked[i][j] = False
                    return True
                if dfs(board,i,j-1,k+1):
                    marked[i][j] = False
                    return True
                marked[i][j]=False
                return False
            else:
                return False

        for i in range(rows):
            for j in range(cols):
                if dfs(board,i,j,0):
                    return True
        return False

if __name__ == '__main__':
    s=Solution()
    print(s.exist([  ['A','B','C','E'],
                     ['S','F','C','S'],
                     ['A','D','E','E']],'ABCB'))