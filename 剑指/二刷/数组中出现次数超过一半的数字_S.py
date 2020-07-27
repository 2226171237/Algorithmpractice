'''
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。

示例 1:
输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
输出: 2
限制：
1 <= 数组长度 <= 50000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def majorityElement(self, nums):
        """
        哈希表
        :type nums: List[int]
        :rtype: int
        """
        hash_map=dict()
        maxCnt=0
        maxNum=nums[0]
        for x in nums:
            hash_map[x]=hash_map.get(x,0)+1
            if maxCnt<hash_map[x]:
                maxCnt=hash_map[x]
                maxNum=x
        return maxNum

    def majorityElement2(self, nums):
        '''
        投票法
        :param nums:
        :return:
        '''
        vote=0
        maxNum=nums[0]
        for x in nums:
            if vote==0:
                maxNum=x
            vote+=1 if x==maxNum else -1
        return maxNum

if __name__ == '__main__':
    s=Solution()
    print(s.majorityElement([1, 2, 3, 2, 2, 2, 5, 4, 2]))
    print(s.majorityElement2([1, 2, 3, 2, 2, 2, 5, 4, 2]))

