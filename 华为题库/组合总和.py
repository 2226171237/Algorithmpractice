'''
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的数字可以无限制重复被选取。

说明：
所有数字（包括 target）都是正整数。
解集不能包含重复的组合。 
示例 1:
输入: candidates = [2,3,6,7], target = 7,
所求解集为:
[
  [7],
  [2,2,3]
]
示例 2:
输入: candidates = [2,3,5], target = 8,
所求解集为:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combination-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def combinationSum(self, candidates, target: int):
        '''
        回溯
        :param list[int] candidates:
        :param int target:
        :return: list[list[int]]
        '''
        result=[]
        def getresult(candidates:list,target:int,path:list,lastsum:int):
            if target<lastsum:
                return
            if target==lastsum:
                result.append(path[:])
            for i,x in enumerate(candidates):
                path.append(x)
                getresult(candidates[i:],target,path,lastsum+x)
                path.pop()

        getresult(candidates,target,[],0)

        return result

if __name__ == '__main__':
    S=Solution()
    print(S.combinationSum([2,3,6,7],7))

