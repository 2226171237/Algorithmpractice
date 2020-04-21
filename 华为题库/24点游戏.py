'''
你有 4 张写有 1 到 9 数字的牌。你需要判断是否能通过 *，/，+，-，(，) 的运算得到 24。

示例 1:
输入: [4, 1, 8, 7]
输出: True
解释: (8-4) * (7-1) = 24
示例 2:
输入: [1, 2, 1, 2]
输出: False
注意:

除法运算符 / 表示实数除法，而不是整数除法。例如 4 / (1 - 2/3) = 12 。
每个运算符对两个数进行运算。特别是我们不能用 - 作为一元运算符。例如，[1, 1, 1, 1] 作为输入时，表达式 -1 - 1 - 1 - 1 是不允许的。
你不能将数字连接在一起。例如，输入为 [1, 2, 1, 2] 时，不能写成 12 + 12 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/24-game
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

from operator import mul,add,sub,truediv

class Solution:
    def judgePoint24(self, nums) -> bool:
        '''
        枚举，回溯
        :param list[int] nums:
        :return:
        '''
        if len(nums)==0:
            return False
        if len(nums)==1:
            return abs(nums[0]-24)<1e-6
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!=j:
                    B=[nums[k] for k in range(len(nums)) if k!=i and k!=j] # 选两个数后剩余的数
                    for opt in (mul,sub,truediv,add):
                        if (opt==mul or opt==add) and j<i: continue # 交换率可裁剪
                        if opt!=truediv or nums[j]:  # 防止除以0
                            B.append(opt(nums[i],nums[j])) # 前两个数的运算结果
                            if self.judgePoint24(B): # 剩余运算
                                return True
                            B.pop() # 回溯
        return False

if __name__ == '__main__':
    S=Solution()
    print(S.judgePoint24([1,9,1,2]))




