'''
0,1,,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字。求出这个圆圈里剩下的最后一个数字。

例如，0、1、2、3、4这5个数字组成一个圆圈，从数字0开始每次删除第3个数字，则删除的前4个数字依次是2、0、4、1，因此最后剩下的数字是3。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''

from collections import deque
class Solution(object):
    def lastRemaining(self, n, m):
        """
        队列实现,超时
        :type n: int
        :type m: int
        :rtype: int
        """
        k=0
        Q=deque()
        for i in range(n):
            k += 1
            if k==m:
                k=0
            else:
                Q.append(i)
        if len(Q)==0:
            return n-1
        while len(Q)>1:
            x=Q.popleft()
            k += 1
            if k==m:
                k=0
            else:
                Q.append(x)
        return Q[0]

    def lastRemaining2(self,n,m):
        '''
        使用数组实现,2068 ms通过
        :param n:
        :param m:
        :return:
        '''
        idx=0
        L=list(range(n))
        while len(L)>1:
            idx=idx+m-1
            if idx>=len(L):
                idx=idx%len(L)
            L.pop(idx)
        return L[0]

    def lastRemaining3(self,n,m):
        ans=0
        for i in range(2,n+1):
            ans=(ans+m)%i
        return ans

if __name__ == '__main__':
    S=Solution()
    print(S.lastRemaining(100,3))
    print(S.lastRemaining2(100, 3))
    print(S.lastRemaining3(100, 3))





