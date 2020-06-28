'''
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。

示例：
输入：nums = [1,2,3,4]
输出：[1,3,2,4]
注：[3,1,2,4] 也是正确的答案之一。
 
提示：
1 <= nums.length <= 50000
1 <= nums[i] <= 10000
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''
class Solution(object):
    def exchange(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result=[0 for _ in range(len(nums))]
        low=0
        high=len(result)-1
        for x in nums:
            if x&1==1:
                result[low]=x
                low+=1
            else:
                result[high]=x
                high-=1
        return result

    def exchange2(self,nums):
        '''双端指针'''
        low=0
        high=len(nums)-1
        while low<high:
            if nums[low]&1==0 and nums[high]&1==1:
                nums[high],nums[low]=nums[low],nums[high]
                low+=1
                high-=1
            elif nums[low]&1==1:
                low+=1
            elif nums[high]&1==0:
                high-=1
        return nums

if __name__ == '__main__':
    s=Solution()
    x=list(range(20))
    import random
    random.shuffle(x)
    print(s.exchange2(x))