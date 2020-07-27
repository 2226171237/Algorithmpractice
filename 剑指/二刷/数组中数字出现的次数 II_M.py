'''
在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。

示例 1：
输入：nums = [3,4,3,3]
输出：4
示例 2：
输入：nums = [9,1,7,9,7,9,7]
输出：1

限制：
1 <= nums.length <= 10000
1 <= nums[i] < 2^31

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-ii-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=set()
        sum1=0
        sum2=0
        for x in nums:
            sum1+=x
            if x not in s:
                s.add(x)
                sum2+=x
        return (3*sum2-sum1)//2

    def singleNumber2(self, nums):
        counts=[0 for _ in range(32)]
        for x in nums:
            for i in range(32):
                counts[i]+=1 if x>>i&1 else 0
        t=0
        for i,x in enumerate(counts):
            x=x%3
            if x==1:
                t+=1<<i
        return t
if __name__ == '__main__':
    s=Solution()
    print(s.singleNumber([3,3,3,4]))
    print(s.singleNumber2([3, 3, 3, 4]))

