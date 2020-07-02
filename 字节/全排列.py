'''
给定一个 没有重复 数字的序列，返回其所有可能的全排列。
'''
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]

        def _permute(nums,i,path):
            if i>=len(nums):
                res.append(path[:])
                return
            for j in range(i,len(nums)):
                nums[i],nums[j]=nums[j],nums[i]
                path.append(nums[i])
                _permute(nums,i+1,path)
                path.pop()
                nums[i],nums[j]=nums[j],nums[i]
        _permute(nums,0,[])
        return res

if __name__ == '__main__':
    s=Solution()
    print(s.permute([1,2,3]))