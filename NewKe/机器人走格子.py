'''
地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，
但是不能进入行坐标和列坐标的数位之和大于k的格子。 例如，当k为18时，机器人能够进入方格（35,37），
因为3+5+3+7 = 18。但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？
'''


def getBitSum(n):
    s=0
    while n:
        s+=n%10
        n//=10
    return s

class Solution:
    def isValid(self,i,j,threshold):
        return getBitSum(i)+getBitSum(j)<=threshold

    def movingCount(self, threshold, rows, cols):
        # write code here
        visited=[[False for _ in range(cols)] for _ in range(rows)]
        return self.slove(visited,threshold,rows,cols,0,0)

    def slove(self,visited,threshld,rows,cols,i,j):
        if i<0 or i>=rows or j<0 or j>=cols or not self.isValid(i,j,threshld) or visited[i][j]:
            return 0
        visited[i][j]=True
        nums=self.slove(visited,threshld,rows,cols,i+1,j)+\
                self.slove(visited, threshld, rows, cols, i-1, j)+\
                self.slove(visited, threshld, rows, cols, i, j-1)+\
                self.slove(visited, threshld, rows, cols, i, j+1)
        return nums+1

if __name__ == '__main__':
    S=Solution()
    print(S.movingCount(5,10,10))
    print(getBitSum(123))

