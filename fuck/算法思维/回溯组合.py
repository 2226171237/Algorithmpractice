
class Solution:
    def combine(self,n,k):
        '''
        返回[1,...,n]的k个元素的所有组合
        '''
        result=[]

        def dfs(start,path):
            if len(path)==k:
                result.append(path[:])
                return
            for i in range(start,n+1):
                path.append(i)
                dfs(i+1,path)
                path.pop()
        dfs(1,[])
        return result
    def permute(self,nums):
        '''输入一个**不包含重复数字**的数组 `nums`，返回这些数字的全部排列。'''
        result=[]
        def _permute(nums,i,path):
            if i==len(nums):
                result.append(path[:])
                return
            for j in range(i,len(nums)):
                nums[i],nums[j]=nums[j],nums[i]
                path.append(nums[i])
                _permute(nums,i+1,path)
                path.pop()
                nums[i], nums[j] = nums[j], nums[i]
        _permute(nums,0,[])
        return result

if __name__ == '__main__':
    s=Solution()
    print(s.combine(5,3))
    print(s.permute([1,2,3]))