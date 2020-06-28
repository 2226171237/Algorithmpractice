'''
给你一个二进制数组 nums ，你需要从中删掉一个元素。
请你在删掉元素的结果数组中，返回最长的且只包含 1 的非空子数组的长度。
如果不存在这样的子数组，请返回 0 。
提示 1：
输入：nums = [1,1,0,1]
输出：3
解释：删掉位置 2 的数后，[1,1,1] 包含 3 个 1 。
示例 2：
输入：nums = [0,1,1,1,0,1,1,0,1]
输出：5
解释：删掉位置 4 的数字后，[0,1,1,1,1,1,0,1] 的最长全 1 子数组为 [1,1,1,1,1] 。

提示：
1 <= nums.length <= 10^5
nums[i] 要么是 0 要么是 1 。
'''


class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        result=0
        a=0
        b=0
        for x in nums:
            if x==1:
                a+=1
                b+=1
                result=max(a,result)
            else:
                a=b
                b=0
        if result==N:
            result-=1
        return result

    def longestSubarray2(self, nums):
        '''滑动窗口法，统计窗口内0的个数，雄安与等于1则扩大窗口，否则滑动窗口'''
        N=len(nums)
        result=0
        zero_num=0
        left=0
        right=0
        while right<N:
            zero_num+=1-nums[right]
            result = max(right - left + 1 - zero_num,result)
            while left<right and zero_num>1:
                if nums[left]==0:
                    zero_num-=1
                left+=1
            right += 1
        return result-1 if result==N else result

if __name__ == '__main__':
    s=Solution()
    print(s.longestSubarray([1,1,1,0,1,1,1,0,1]))
    print(s.longestSubarray2([1, 1, 1, 0, 0, 1, 0, 0, 1]))