'''
一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。
请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。

限制：
2 <= nums.length <= 10000
'''

class Solution(object):
    def singleNumbers(self, nums):
        """
        异或的方法
        :type nums: List[int]
        :rtype: List[int]
        """
        res=0
        for x in nums:
            res^=x
        i=0
        while (res&1<<i)==0:
            i+=1
        tmp_res=res
        for x in nums:
            if x&(1<<i)==0:
                tmp_res ^=x
        return [tmp_res,res^tmp_res]

if __name__ == '__main__':
    S=Solution()
    print(S.singleNumbers([1,2,10,4,1,4,3,3]))


