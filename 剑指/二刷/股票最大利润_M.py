'''
假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？

示例 1:
输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/gu-piao-de-zui-da-li-run-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def maxProfit(self, prices):
        """
        最长路径
        :type prices: List[int]
        :rtype: int
        """
        N=len(prices)
        if N==0:
            return 0
        # 构图
        G=[[] for _ in range(N+2)]
        s,t=N,N+1
        for i in range(N):
            G[s].append((s,i,-prices[i]))
            G[i].append((i,t,prices[i]))
            if i<N-1:
                G[i].append((i,i+1,0))

        # 拓扑排序
        order=[]
        distTo=[float('-inf') for _ in range(N+2)]
        distTo[s]=0
        marked=[False for _ in range(N+2)]
        def _dfs(G,v):
            marked[v]=True
            for e in G[v]:
                w=e[1]
                if not marked[w]:
                    _dfs(G,w)
            order.append(v)
        for v in range(N+2):
            if not marked[v]:
                _dfs(G,v)
        # 最长路径
        def _relax(G,v):
            for e in G[v]:
                w=e[1]
                if distTo[w]<distTo[v]+e[-1]:
                    distTo[w]=distTo[v]+e[-1]
        for v in order[::-1]:
            _relax(G,v)
        return distTo[t]

    def maxProfit2(self,prices):
        '''动态规划'''
        N=len(prices)
        if N==0:
            return 0
        m=prices[0]
        p=0
        for x in prices[1:]:
            p=max(p,x-m)
            m = min(m, x)
        return p


if __name__ == '__main__':
    s=Solution()
    print(s.maxProfit([7,1,5,3,6,4]))
    print(s.maxProfit2([7,1,5,3,6,4]))

