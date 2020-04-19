'''
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。
如果没有任何一种硬币组合能组成总金额，返回 -1。

示例 1:
输入: coins = [1, 2, 5], amount = 11
输出: 3
解释: 11 = 5 + 5 + 1
示例 2:
输入: coins = [2], amount = 3
输出: -1
 
说明:
你可以认为每种硬币的数量是无限的。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/coin-change
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

import functools
class Solution:
    def coinChange(self, coins,amount: int) -> int:
        '''
        递归,超时
        :param list[int] vcoins:
        :param amount:
        :return:
        '''
        lens=len(coins)
        if lens==0 or amount==0:
            return 0
        if lens==0 and amount>0:
            return -1

        def _coinChange(coins,amount,count):
            if amount==0:
                return count
            if amount<0:
                return 2**31
            mins=2**31
            for x in coins:
                mins=min(mins,_coinChange(coins,amount-x,count+1))
            return mins

        count= _coinChange(coins,amount,0)
        if count==2**31:
            return -1
        else:
            return count

    def coinChange2(self, coins,amount: int) -> int:
        '''
        动态规划，动态规划-自上而下 [通过]
        F(S):组成面值为S需要的最少硬币。
        F(S)=F(S-C)+1,C为组成S选的最后一个硬币，由于C不知，所以可以枚举所有的C，选择最小的F(S).
        F(S)=min_i(F(S-c_i)+1), c_i in coins.
        基本情况：F(0)=0;F(S)=-1 if n==0
        :param list[int] vcoins:
        :param amount:
        :return:
        '''
        lens=len(coins)
        if lens==0 or amount==0:
            return 0
        if lens==0 and amount>0:
            return -1
        @functools.lru_cache(amount)
        def _coinChange(amount:int):
            if amount==0:
                return 0
            if amount<0:
                return -1
            Mins=2**31
            for x in coins:
                res=_coinChange(amount-x)
                if res>=0 and res<Mins:  # 存在
                    Mins=res+1
            return -1 if Mins==2**31 else Mins

        return _coinChange(amount)




if __name__ == '__main__':
    S=Solution()
    print(S.coinChange2([186,419,83,408],6249))

