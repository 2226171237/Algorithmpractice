'''
给定一个数组 A[0,1,…,n-1]，请构建一个数组 B[0,1,…,n-1]，其中 B 中的元素 B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]。不能使用除法。

示例:
输入: [1,2,3,4,5]
输出: [120,60,40,30,24]
提示：
所有元素乘积之和不会溢出 32 位整数
a.length <= 100000
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/gou-jian-cheng-ji-shu-zu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def constructArr(self, a):
        """
        :type a: List[int]
        :rtype: List[int]
        """
        N=len(a)
        b=[1 for _ in range(N)]
        i=1
        while i<N:
            b[i]*=b[i-1]*a[i-1]
            i+=1
        t=1
        i=N-1
        while i>=0:
            b[i]*=t
            t*=a[i]
            i-=1
        return b

if __name__ == '__main__':
    s=Solution()
    print(s.constructArr([1,2,3,4,5]))