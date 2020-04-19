'''
0,1,,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字。求出这个圆圈里剩下的最后一个数字。
例如，0、1、2、3、4这5个数字组成一个圆圈，从数字0开始每次删除第3个数字，则删除的前4个数字依次是2、0、4、1，因此最后剩下的数字是3。

示例 1：
输入: n = 5, m = 3
输出: 3

示例 2：
输入: n = 10, m = 17
输出: 2
 

限制：
1 <= n <= 10^5
1 <= m <= 10^6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from collections import deque
class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        '''
        双端队列,超时了
        :param n:
        :param m:
        :return:
        '''
        Q=deque()
        k=1
        for x in range(n):
            if k<m:
                Q.append(x)
                k+=1
            else:
                k=1
        if len(Q)==0:  #处理m=1
            return n-1
        while len(Q)!=1:
            t=Q.popleft()
            if k<m:
                Q.append(t)
                k+=1
            else:
                k=1
        return Q[0]
    def lastRemaining2(self, n: int, m: int) -> int:
        '''
        约瑟夫环
        f(n,m)=(f(n-1,m)+m)%n
        n=1是 f=0
        :param n:
        :param m:
        :return:
        '''
        pos=0
        for i in range(2,n+1): # 到n 正好是最后一个被杀掉的人
            pos=(pos+m)%i
        return pos


if __name__ == '__main__':
    S=Solution()
    print(S.lastRemaining(70866,11))
    print(S.lastRemaining2(5, 3))