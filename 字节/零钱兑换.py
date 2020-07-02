'''
给定不同面额的硬币 coins 和一个总金额 amount。
编写一个函数来计算可以凑成总金额所需的最少的硬币个数。
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
from functools import lru_cache
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        @lru_cache(amount)
        def find(amount):
            if amount==0:
                return 0
            if amount<0:
                return -1
            Mins=2**31
            for c in coins:
                num=find(amount-c)
                if num<0:
                    continue
                else:
                    Mins=min(Mins,1+num)
            if Mins==2**31:
                return -1
            return Mins
        return find(amount)

if __name__ == '__main__':
    s=Solution()
    print(s.coinChange([186,419,83,408],6249))