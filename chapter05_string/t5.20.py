'''
如何在二维数组中寻找最短路线？
虚招一条从左上角a[0,0]，到右下角a[m-1][n-1]的路线，使得沿途经过的数的整数和最小。
'''

# 递归

def minPath1(arr,i,j):
    if 0==i and 0==j:
        return arr[0][0]

    if 0<i and 0<j:
        s1=minPath1(arr,i-1,j)
        s2=minPath1(arr,i,j-1)
        s=min(s1,s2)

    elif i==0 and j>0:
        s=minPath1(arr,i,j-1)
    elif j==0 and i>0:
        s=minPath1(arr,i-1,j)

    return arr[i][j]+s


# 动态规划，有负数就不行了，且打印的并不是路径。
def minPath2(arr):
    m=len(arr)
    n=len(arr[0])
    M=[[0 for _ in range(n)] for _ in range(m)]
    Path = [[(0,0) for _ in range(n)] for _ in range(m)]
    M[0][0]=arr[0][0]
    i=1
    while i<n:
        M[0][i]=M[0][i-1]+arr[0][i]
        Path[0][i]=(0,i-1)
        i+=1
    i = 1
    while i < m:
        M[i][0] =M[i-1][0]+ arr[i][0]
        Path[i][0]=(i-1,0)
        i += 1

    i=1
    while i<m:
        j=1
        while j<n:
            if M[i-1][j]>M[i][j-1]:
                M[i][j]=M[i][j-1]+arr[i][j]
                Path[i][j]=(i,j-1)
            else:
                M[i][j] = M[i-1][j] + arr[i][j]
                Path[i][j] = (i-1, j)
            j+=1
        i+=1
    p=[(2,2)]
    while p[-1]!=(0,0):
        p.append(Path[p[-1][0]][p[-1][1]])
    return M[-1][-1],p

if __name__ == '__main__':
    arr=[[1,4,3],
         [8,7,5],
         [2,1,5]]
    print(minPath1(arr,2,2))
    print(minPath2(arr))