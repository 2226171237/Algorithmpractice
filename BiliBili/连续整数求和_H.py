'''
给定一个正整数 N，试求有多少组连续正整数满足所有数字之和为 N?
示例 1:
输入: 5
输出: 2
解释: 5 = 5 = 2 + 3，共有两组连续整数([5],[2,3])求和后为 5。
示例 2:
输入: 9
输出: 3
解释: 9 = 9 = 4 + 5 = 2 + 3 + 4
示例 3:
输入: 15
输出: 4
解释: 15 = 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5
说明: 1 <= N <= 10 ^ 9
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/consecutive-numbers-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        cnt=1
        x=1
        while x<N//2+1:
            b24ac=((2*x-1)**2+8*N)**0.5
            k=(1-2*x)+b24ac
            if k>0 and k%2==0:
                cnt+=1
            x+=1
        return cnt

    def consecutiveNumbersSum2(self, N):
        cnt=0
        left=0
        right=1
        sum=0
        while right<=N//2+1:
            sum+=right
            while sum>N:
                sum-=left
                left+=1
            if sum==N:
                cnt+=1
                sum-=left
                left+=1
            right+=1
        return cnt+ (1 if right!=N+1 else 0)

    def consecutiveNumbersSum3(self, N):
        cnt=0
        i=1
        while N>0:
            if N%i==0:
                cnt+=1
            N-=i
            i+=1
        return cnt

if __name__ == '__main__':
    s=Solution()
    # print(s.consecutiveNumbersSum(72316829))
    print(s.consecutiveNumbersSum2(72316829))
    print(s.consecutiveNumbersSum3(72316829))
