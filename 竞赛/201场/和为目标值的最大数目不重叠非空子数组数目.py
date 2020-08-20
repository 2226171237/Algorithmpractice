class Solution(object):
    def maxNonOverlapping(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        cnt=0
        i=0
        minI=-1
        while i<len(nums):
            sum=0
            for j in range(i,minI,-1):
                sum+=nums[j]
                if sum==target: # 只找i前面最近满足的j
                    cnt+=1
                    minI=i
                    break
            i+=1
        return cnt

if __name__ == '__main__':
    s=Solution()
    print(s.maxNonOverlapping([1,1,1,1,1],2))

