'''
给你一个整数数组 arr 和一个整数 k ，其中数组长度是偶数，值为 n 。
现在需要把数组恰好分成 n / 2 对，以使每对数字的和都能够被 k 整除。
如果存在这样的分法，请返回 True ；否则，返回 False 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/check-if-array-pairs-are-divisible-by-k
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def canArrange(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: bool
        """
        arr=[x%k for x in arr]
        d=[0 for _ in range(k)]
        for x in arr:
            d[x]+=1
        if d[0]%2!=0:
            return False
        for x in range(1,k):
            if (d[x]+d[k-x])%2!=0:
                return False
        return True


if __name__ == '__main__':
    s=Solution()
    print(s.canArrange([1,2,3,4,5,6],7))