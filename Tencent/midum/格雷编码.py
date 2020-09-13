'''
格雷编码是一个二进制数字系统，在该系统中，两个连续的数值仅有一个位数的差异。
给定一个代表编码总位数的非负整数 n，打印其格雷编码序列。即使有多个不同答案，你也只需要返回其中一种。
格雷编码序列必须以 0 开头。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/gray-code
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res=[0,1]
        for i in range(1,n):
            j=len(res)-1
            tmp=1<<i
            while j>=0:
                res.append(res[j]^tmp)
                j-=1
        return res

if __name__ == '__main__':
    s=Solution()
    print(s.grayCode(4))
