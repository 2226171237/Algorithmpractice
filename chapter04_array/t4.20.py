# -*-coding=utf-8 -*-
'''
如何获取最好的矩阵链相乘方法？
给定一个矩阵序列，找到最有效的方式将这些矩阵相乘在一起。给定表示矩阵的数组p,
使得第i个矩阵Ai的维数为p[i-1]Xp[i]。编写一个函数MatrixChainOrder(),该函数
应该返回乘法运算所得的最小乘法数。
输入：p=(40,20,30,10,30)
输出：26000
有4个大小为40x20,20x30，30x10和10x30的矩阵。假设这四个矩阵为A,B,C,D,该函数的执行方法可以使执行乘法运算的次数最少。
'''

# 递归
def maxtrixChainOrder(p,i,j):
    if i==j:
        return 0
    mins=2**32
    k=i  # k为括号的位置
    while k<j:
        counts=maxtrixChainOrder(p,i,k)+maxtrixChainOrder(p,k+1,j)+p[i-1]*p[k]*p[j]
        if counts<mins:
            mins=counts
        k+=1
    return mins

if __name__ == '__main__':
    p=[40,20,30,10,30]
    print(maxtrixChainOrder(p,1,4))

