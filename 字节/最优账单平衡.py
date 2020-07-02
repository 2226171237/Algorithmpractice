'''
一群朋友在度假期间会相互借钱。比如说，小爱同学支付了小新同学的午餐共计 10 美元。
如果小明同学支付了小爱同学的出租车钱共计 5 美元。
我们可以用一个三元组 (x, y, z) 表示一次交易，表示 x 借给 y 共计 z 美元。
用 0, 1, 2 表示小爱同学、小新同学和小明同学（0, 1, 2 为人的标号），上述交易可以表示为 [[0, 1, 10], [2, 0, 5]]。

给定一群人之间的交易信息列表，计算能够还清所有债务的最小次数。

注意：
一次交易会以三元组 (x, y, z) 表示，并有 x ≠ y 且 z > 0。
人的标号可能不是按顺序的，例如标号可能为 0, 1, 2 也可能为 0, 2, 6。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/optimal-account-balancing
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def minTransfers(self, transactions):
        """
        :type transactions: List[List[int]]
        :rtype: int
        """
