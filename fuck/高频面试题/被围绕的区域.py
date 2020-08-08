
# DFS
def solve1(board):
    rows=len(board)
    cols=len(board[0])
    def isValid(i,j):
        return i>=0 and i<rows and j>=0 and j<cols and board[i][j]=='O'
    def dfs(i,j):
        if not isValid(i,j):
            return
        board[i][j]='#'
        dfs(i+1,j)
        dfs(i,j+1)
        dfs(i-1,j)
        dfs(i,j-1)
    for i in range(rows):
        for j in range(cols):
            edge=i==0 or j==0 or i==rows-1 or j==cols-1
            if edge and board[i][j]=='O':
                dfs(i,j)
    for i in range(rows):
        for j in range(cols):
            if board[i][j]=='O':
                board[i][j]='X'
            elif board[i][j]=='#':
                board[i][j]='O'
