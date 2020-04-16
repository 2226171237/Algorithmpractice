'''
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一个格子开始，
每一步可以在矩阵中向左，向右，向上，向下移动一个格子。如果一条路径经过了矩阵中的某一个格子，则该路径不能再进入该格子。 
例如:
[[a,b,c,e],
 [s,f,c,s],
 [a,d,e,e]]
矩阵中包含一条字符串"bcced"的路径，但是矩阵中不包含"abcb"路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，
路径不能再次进入该格子。
'''


class Solution:

    def hasPath(self, matrix, rows, cols, path):
        flags=[False for _ in range(len(matrix))]
        for i in range(rows):
            for j in range(cols):
                if self.judge(matrix,flags,i,j,rows,cols,path,0):
                    return True
        return False

    def judge(self,matrix,flags,i,j,rows,cols,path,k):
        index=i*cols+j
        # 越界，或以访问，或字符不对。
        if  i<0 or i>=rows or j<0 or j>=cols or flags[index] or matrix[index]!=path[k]:
            return False
        if k==len(path)-1:
            return True
        flags[index]=True
        # 四个方向走
        if (self.judge(matrix,flags,i+1,j,rows,cols,path,k+1) or
            self.judge(matrix,flags,i-1,j,rows,cols,path,k+1) or
            self.judge(matrix, flags, i, j-1, rows, cols, path, k + 1) or
            self.judge(matrix, flags, i, j+1, rows, cols, path, k + 1) ):
            return True
        else:
            # 失败则回退
            flags[index]=False
            return False

if __name__ == '__main__':
    S=Solution()
    print(S.hasPath("ABCESFCSADEE",3,4,"SEE"))