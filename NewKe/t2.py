'''
题目描述
对于一个给定的正整数组成的数组 a[] ，如果将 a 倒序后数字的排列与 a 完全相同，我们称这个数组为“回文”的。
例如， [1, 2, 3, 2, 1] 的倒序是他自己，所以是一个回文的数组；而 [1, 2, 3, 1, 2] 的倒序是 [2, 1, 3, 2, 1] ，
所以不是一个回文的数组。对于任意一个正整数数组，如果我们向其中某些特定的位置插入一些正整数，那么我们总是能构
造出一个回文的数组。输入一个正整数组成的数组，要求你插入一些数字，使其变为回文的数组，且数组中所有数字的和尽
可能小。输出这个插入后数组中元素的和。例如，对于数组 [1, 2, 3, 1, 2] 我们可以插入两个 1 将其变为回文的数组
 [1, 2, 1, 3, 1, 2, 1] ，这种变换方式数组的总和最小，为 11 ，所以输出为 11 。
'''
from collections import deque

class Solution:
    def reLoopAray(self, L):

        def _loopArray(L):
            n = len(L)
            if n == 1:
                return L[0]
            if n == 0:
                return 0
            if L[0] == L[-1]:
                return L[0] + L[-1] + _loopArray(L[1:-1])
            else:
                A = L[0] + L[0] + _loopArray(L[1:])
                B = L[-1] + L[-1] + _loopArray(L[:-1])
                return min(A, B)

        return _loopArray(L)

    def loopAray(self, L):
        n = len(L)
        if n == 0:
            return 0
        if n == 1:
            return L[0]
        P = [[0 for _ in range(n)] for _ in range(n)]
        i = 0
        while i < n:
            P[i][i] = L[i]
            i += 1
        k = 1
        while k < n:
            i = 0
            j = k
            while i < n and j < n:
                if L[i]!=L[j]:
                    P[i][j] = min(L[i] + L[i] + P[i + 1][j], L[j] + L[j] + P[i][j - 1])
                else:
                    P[i][j]=P[i+1][j-1]+L[i]+L[i]
                i += 1
                j += 1
            k+=1
        for p in P:
            print(p)
        return P[0][n - 1]



if __name__ == '__main__':
    S=Solution()
    L=[1,2,3,1,2,3,5,4]
    print(S.loopAray(L))