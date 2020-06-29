'''
给你一个整数数组 nums 和一个整数 target 。
请你统计并返回 nums 中能满足其最小元素与最大元素的 和 小于或等于 target 的 非空 子序列的数目。
由于答案可能很大，请将结果对 10^9 + 7 取余后返回。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution(object):
    def numSubseq(self, nums, target):
        """
        递归
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        result=[0]
        def find(nums,i,MIN,MAX,target):
            if i>=len(nums):
                return
            if min(MIN,nums[i])+max(MAX,nums[i])<=target:
                result[0]+=1
            # 选i
            find(nums, i + 1, min(MIN, nums[i]), max(MAX, nums[i]), target)
            # 不选i
            find(nums, i + 1, MIN, MAX, target)

        MIN=target
        MAX=0
        find(nums,0,MIN,MAX,target)
        return result[0] % (10**9 + 7)

    def numSubseq2(self, nums, target):
        '''排序+递归+记忆化'''
        nums=sorted(nums)
        memory=dict()
        def find(nums,low,high,target):
            if low>high:
                return 0
            if nums[low]+nums[high]<=target:
                if (low,high) in memory:
                    return memory[(low,high)]
                else:
                    A=find(nums,low+1,high,target)
                    B=find(nums,low,high-1,target)
                    C=find(nums,low+1,high-1,target)
                    cnt=2**(max(high-low-1,0))+A+B-C
                    memory[(low,high)]=cnt
                    return cnt
            else:
                return find(nums,low,high-1,target)
        cnt=find(nums,0,len(nums)-1,target)
        return cnt%(10**9+7)

    def numSubseq3(self, nums, target):
        '''排序+双指针'''
        nums=sorted(nums)
        cnt=0
        left=0
        right=len(nums)-1
        while left<=right:
            if nums[left]+nums[right]<=target:
                cnt+=2**(right-left)   # (从left到right 中取0，1，2，，，，left-right个)
                left+=1
            else:
                right-=1
        return cnt%(10**9+7)

if __name__ == '__main__':
    s=Solution()
    print(s.numSubseq([7,10,7,3,7,5,4],12))
    print(s.numSubseq2([7,10,7,3,7,5,4],12))
    print(s.numSubseq3([7, 10, 7, 3, 7, 5, 4], 12))