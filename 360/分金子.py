'''
A、B两伙马贼意外地在一片沙漠中发现了一处金矿，双方都想独占金矿，但各自的实力都不足以吞下对方，
经过谈判后，双方同意用一个公平的方式来处理这片金矿。处理的规则如下：他们把整个金矿分成n段，
由A、B开始轮流从最左端或最右端占据一段，直到分完为止。
马贼A想提前知道他们能分到多少金子，因此请你帮忙计算他们最后各自拥有多少金子?（两伙马贼均会采取对己方有利的策略）

输入
测试数据包含多组输入数据。输入数据的第一行为一个正整数T(T<=20)，表示测试数据的组数。
然后是T组测试数据，每组测试数据的第一行包含一个整数n，下一行包含n个数（n <= 500 ），
表示每段金矿的含金量，保证其数值大小不超过1000。
样例输入
2
6
4 7 2 9 5 2
10
140 649 340 982 105 86 56 610 340 879

输出
对于每一组测试数据，输出一行"Case #id: sc1 sc2"，表示第id组数据时马贼A分到金子数量为sc1，马贼B分到金子数量为sc2。详见样例。
样例输出
Case #1: 18 11
Case #2: 3206 981
'''
import sys
from __future__ import print_function
from __future__ import  division

class Solution:
    def solve(self,nums):
        N=len(nums)
        first=[[0 for _ in range(N)] for _ in range(N)]
        second=[[0 for _ in range(N)] for _ in range(N)]
        for i in range(N):
            first[i][i]=nums[i]
            second[i][i]=0
        for jj in range(1,N):
            for i in range(0,N-jj):
                j=i+jj
                left=nums[i]+second[i+1][j]
                right=nums[j]+second[i][j-1]
                if left>right:
                    first[i][j]=left
                    second[i][j]=first[i+1][j]
                else:
                    first[i][j]=right
                    second[i][j]=first[i][j-1]
        return first[0][-1],second[0][-1]

T=int(sys.stdin.readline().strip())
for t in range(1,T+1):
    n=int(sys.stdin.readline().strip())
    nums=sys.stdin.readline().strip().split(' ')
    nums=[int(x) for x in nums]
    a,b=solve(nums)
    print('Case #%d:%d %d' % (t,a,b))

if __name__ == '__main__':
    s=Solution()
    print(s.solve([4,7,2,9,5,2]))