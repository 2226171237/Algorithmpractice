'''
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
注意：给定 n 是一个正整数。

示例 1：
输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶

示例 2：
输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/climbing-stairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def climbStairs1(self, n: int) -> int:
        # 递归,超时了
        if n<=0:
            return 0
        if n<=3:
            return n
        return self.climbStairs1(n-1)+self.climbStairs1(n-2)  # 跳到n-1的数，没有跳到n-1的数,其实就是斐波那契数列

    def climbStairs2(self, n: int) -> int:
        # 动态规划,斐波那契数列
        if n<=3:
            return n
        prepre,pre=1,2
        for i in range(3,n+1):
            t=pre
            pre=pre+prepre
            prepre=t
        return pre

if __name__ == '__main__':
    S=Solution()
    print(S.climbStairs1(10))
    print(S.climbStairs2(10))
