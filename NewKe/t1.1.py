'''
字节跳到，第一题：
P为给定的二维平面整数点集。定义 P 中某点x，如果x满足 P 中任意点都不在 x 的右上方区域内（横纵坐标都大于x），则称其为“最大的”。
求出所有“最大的”点的集合。（所有点的横坐标和纵坐标都不重复, 坐标轴范围在[0, 1e9) 内）
如下图：实心点为满足条件的点的集合。请实现代码找到集合 P 中的所有 ”最大“ 点的集合并输出。
'''


# 思路解析：
# 题目要求我们需要输出的是，存在满足没有(x,y)同时大于他的点。
# 因此，通过分析可以知道，如果先将x按降序排序。那么我们每次只需要更新最大的y就好了。
# 因为，之后的出现的x不可能会比之前的大，那么满足输出的情况只要一种了，
# 就是之后的某个点的y比之前的大。

import matplotlib.pyplot as plt


def partition(L,low,high):
    base=L[low]
    while low<high:
        while low<high and L[high][0]>base[0]:
            high-=1
        L[low]=L[high]
        while low<high and L[low][0]<=base[0]:
            low+=1
        L[high]=L[low]
    L[low]=base
    return low

def qsort(L,low,high):
    if low>=high:
        return
    ind=partition(L,low,high)
    qsort(L,low,ind-1)
    qsort(L,ind+1,high)


def main(L):
    n=len(L)
    # 按x的降序进行排序
    qsort(L,0,n-1)
    result=[L[-1]]
    i=n-2
    while i>=0:
        if L[i][1]>result[-1][1]:
            result.append(L[i])
        i-=1
    return result


if __name__ == '__main__':
    import random
    x=[random.randint(1,100) for _ in range(20)]
    y=[random.randint(1,100) for _ in range(20)]
    L=list(zip(x,y))
    plt.scatter(x,y)
    result=main(L)
    print(result)
    x=[a[0] for a in result]
    y=[a[1] for a in result]
    plt.scatter(x,y)
    plt.show()
