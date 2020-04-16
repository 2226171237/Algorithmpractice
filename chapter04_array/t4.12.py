#-*-coding=utf-8 -*-
'''
如何对数组进行旋转？
请实现方法：print_rotate_matrix(intmatrix,int n) ，该方法用于将一个n*n的二维数组逆时针旋转45度，后打印，
如：
[[1,2,3]                 3                 3
[4,5,6]    --旋转--->  2   6      --打印-->2 6
[7,8,9]]             1   5   9             1 5 9
                       4   8               4 8
                         7                 7
'''
def print_rotate_matrix(marix):
    n=len(marix)
    # 打印上半部分
    i=0
    for i in range(n-1):
        j=0
        while j<i+1:
            print(marix[j][n-i-1+j],end=' ')
            j+=1
        print('\n',end='')
    # 打印下半部分
    i=0
    for i in range(n):
        j=0
        k=i
        while j<n-i:
            print(marix[k][j],end=' ')
            j+=1
            k+=1
        print('\n',end='')

if __name__ == '__main__':
    matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    print_rotate_matrix(matrix)
