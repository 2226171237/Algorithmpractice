'''
给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。
一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。
示例 1:
输入: 12258
输出: 5
解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"
提示：
0 <= num < 2^31
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

def splitNum(num):
    nums=[]
    while num:
        num,s=num//10,num%10
        nums.append(s)
    return nums[::-1]

class Solution(object):
    def translateNum(self, num):
        """
        :type num: int
        :rtype: int
        """
        nums=splitNum(num)
        P=[0 for _ in range(len(nums))]
        P[0]=1
        i=1
        while i<len(nums):
            P[i]=P[i-1]
            if nums[i-1]==1:
                P[i]+=P[i-2] if i-2>=0 else 1
            elif nums[i-1]==2 and 0<=nums[i]<=5:
                P[i] += P[i - 2] if i - 2 >= 0 else 1
            i+=1
        return P[-1]

if __name__ == '__main__':
    s=Solution()
    print(s.translateNum(12258))





