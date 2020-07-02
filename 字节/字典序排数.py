'''
给定一个整数 n, 返回从 1 到 n 的字典顺序。

例如，
给定 n =1 3，返回 [1,10,11,12,13,2,3,4,5,6,7,8,9] 。
请尽可能的优化算法的时间复杂度和空间复杂度。 输入的数据 n 小于等于 5,000,000。
'''
class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        def dfs(root,n,result):
            if root>n:
                return
            if root>0:
                result.append(root)
            start=1 if root==0 else 0
            for i in range(start,10):
                dfs(root*10+i,n,result)

        result=[]
        dfs(0,n,result)
        return result

if __name__ == '__main__':
    s=Solution()
    print(s.lexicalOrder(100))