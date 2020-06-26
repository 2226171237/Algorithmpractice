'''
从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。2～10为数字本身，A为1，J为11，Q为12，K为13，
而大、小王为 0 ，可以看成任意数字。A 不能视为 14。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/bu-ke-pai-zhong-de-shun-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution(object):
    def isStraight(self, nums):
        """
        没有重复，则最大值减最小值小于等于4
        :type nums: List[int]
        :rtype: bool
        """
        p=[0 for _ in range(14)]
        mins=14
        maxs=-1
        for x in nums:
            maxs=max(maxs,x)
            if x<mins and x!=0:
                mins=x
            p[x]+=1
            if x!=0 and p[x]>1:
                return False

        if maxs-mins>4:
            return False
        else:
            return True


if __name__ == '__main__':
    s=Solution()
    print(s.isStraight([0,0,1,2,5]))