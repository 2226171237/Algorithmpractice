'''
输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。
序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。

示例 1：
输入：target = 9
输出：[[2,3,4],[4,5]]

示例 2：
输入：target = 15
输出：[[1,2,3,4,5],[4,5,6],[7,8]]
 
限制：
1 <= target <= 10^5
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def findContinuousSequence(self, target):
        """
        滑动窗口
        :type target: int
        :rtype: List[List[int]]
        """
        begin=1
        wid_sum=1
        end=1
        result=[]
        while end<=target//2+1:
            if wid_sum<target:
                end+=1
                wid_sum+=end
            elif wid_sum==target:
                result.append(list(range(begin,end+1)))
                wid_sum-=begin
                begin += 1
            else:
                wid_sum-=begin
                begin+=1
        return result

if __name__ == '__main__':
    s=Solution()
    print(s.findContinuousSequence(1))


