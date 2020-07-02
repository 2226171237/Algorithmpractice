'''
给定整数 n 和 k，找到 1 到 n 中字典序第 k 小的数字。

注意：1 ≤ k ≤ n ≤ 10^9。

示例 :
输入:
n: 13   k: 2
输出:
10
解释:
字典序的排列是 [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]，所以第二小的数字是 10。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/k-th-smallest-in-lexicographical-order
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):

    def getcout(self,root,n):
        '''找root和他同层临近的兄弟结点 root+1之间结点个数'''
        brother=root+1
        cnt=0
        while root<=n:
            cnt+=min(brother,n+1)-root
            root*=10
            brother*=10
        return cnt

    def dfs(self,root,n,k):
        if k==0:
            return root
        cnt=self.getcout(root,n)
        if cnt>k:
            return self.dfs(10*root,n,k-1)
        else:
            return self.dfs(root+1,n,k-cnt)

    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        return self.dfs(1,n,k-1)

if __name__ == '__main__':
    s=Solution()
    print(s.findKthNumber(13,2))

