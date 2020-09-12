


def printMatrix(m,n):
    matrix=[[0 for _ in range(n)] for _ in range(m)]
    t=0
    rows=max(m,n)*2
    for ii in range(rows):
        for j in range(n):
          i=ii-j
          if 0<=i<m and 0<=j<n:
              t+=1
              matrix[i][j]=t
    return matrix


import sys
# m,n=[int(x) for x in sys.stdin.readline().strip().split(' ')]
print(printMatrix(1,3))
