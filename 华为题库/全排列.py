'''
给定一个 没有重复 数字的序列，返回其所有可能的全排列。

示例:
输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutations
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def permute(self, nums):
        '''
        递归，交换
        :param list[int] nums:
        :return: list[list[int]]
        '''
        result=[]
        def _permute(nums,i,path):
            if i==len(nums):
                result.append(path[:])
                return
            for j in range(i,len(nums)):
                nums[i],nums[j]=nums[j],nums[i]  # 交换
                t=path[:]
                t.append(nums[i])
                _permute(nums,i+1,t)  # 子序处理
                nums[i], nums[j] = nums[j], nums[i] # 复位
        _permute(nums,0,[])
        return result

if __name__ == '__main__':
    S=Solution()
    print(S.permute([1,2,3,4]))


