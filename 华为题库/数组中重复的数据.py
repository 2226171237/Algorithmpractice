'''
给定一个整数数组 a，其中1 ≤ a[i] ≤ n （n为数组长度）, 其中有些元素出现两次而其他元素出现一次。
找到所有出现两次的元素。
你可以不用到任何额外空间并在O(n)时间复杂度内解决这个问题吗？

示例：
输入:
[4,3,2,7,8,2,3,1]
输出:
[2,3]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-all-duplicates-in-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def findDuplicates(self, nums):
        '''
        哈希表
        :param list[int] nums:
        :return: list[int]
        '''
        hashmap=dict()
        for x in nums:
            hashmap[x]=hashmap.get(x,0)+1
        result=[]
        for k in hashmap:
            if hashmap[k]==2:
                result.append(k)
        return result

    def findDuplicates2(self, nums):
        '''
        1. 找到数字i时，将位置i-1处的数字翻转为负数。
        2. 如果位置i-1 上的数字已经为负，则i是出现两次的数字。
        :param list[int] nums:
        :return: list[int]
        '''
        result=[]
        for i in range(len(nums)):
            index=abs(nums[i])-1
            if nums[index]<0:
                result.append(abs(nums[i]))
            nums[index]=-nums[index]
        return result

if __name__ == '__main__':
    S=Solution()
    print(S.findDuplicates([4,3,2,7,8,2,3,1]))
    print(S.findDuplicates2([4, 3, 2, 7, 8, 2, 3, 1]))