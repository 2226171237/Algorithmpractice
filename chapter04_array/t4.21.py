# -*-coding=utf-8 -*-
'''
如何求解迷宫问题？
给定一个大小为NXN的迷宫，一只老鼠需要从迷宫的左上角走到迷宫的右下角，
老鼠只能向两个方向移动：向右和向下。在迷宫中，0表示没路，1表示有路。
请给出算法，求一个合理的路径。
'''


# 回溯法
class Maze:
    def __init__(self):
        self.N=4

    def printSolution(self,sol):
        i=0
        while i<self.N:
            j=0
            while j<self.N:
                print(sol[i][j],end=' ')
                j+=1

            print('')
            i+=1

    def isSafe(self,maze,x,y):
        return x>=0 and x<self.N and y>=0 and y<self.N and maze[x][y]==1

    def getPath(self,maze,x,y,sol):
        if x==self.N-1 and y==self.N-1:
            sol[x][y]=1
            return True
        if self.isSafe(maze,x,y):
            sol[x][y]=1
            if self.getPath(maze,x+1,y,sol):
                return True
            if self.getPath(maze,x,y+1,sol):
                return True
            sol[x][y]=0
            return False
        return False

if __name__ == '__main__':
    rat=Maze()
    maze=[[1,0,0,0],
          [1,1,0,1],
          [0,1,0,0],
          [1,1,1,1]]
    sol=[[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]
    if not  rat.getPath(maze,0,0,sol):
        print('error')
    else:
        rat.printSolution(sol)
