'''
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。

示例 1:
输入: ["flower","flow","flight"]
输出: "fl"

示例 2:
输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。

说明:
所有输入只包含小写字母 a-z 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-common-prefix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def getCommonPrefix(self,s1,s2):
        if len(s1)==0 or len(s2)==0:
            return ''
        i=0
        while i<len(s1) and i<len(s2) and s1[i]==s2[i]:
            i+=1
        return s1[:i]

    def longestCommonPrefix(self, strs):
        '''
        两两查找
        :param list[str] strs:
        :return: str
        '''
        result=strs[0]
        for s in strs[1:]:
            result=self.getCommonPrefix(result,s)
        return result

    def longestCommonPrefix2(self, strs):
        '''
        分治
        :param strs:
        :return:
        '''
        if len(strs)==0:
            return ''
        def fun(strs,low,high):
            if low==high:
                return strs[low]
            mid=(low+high)//2
            left=fun(strs,low,mid)
            right=fun(strs,mid+1,high)
            return self.getCommonPrefix(left,right)
        return fun(strs,0,len(strs)-1)
if __name__ == '__main__':
    S=Solution()
    print(S.longestCommonPrefix(["flower","flow","flight"]))
    print(S.longestCommonPrefix2(["flower", "flow", "flight"]))