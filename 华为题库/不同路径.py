'''
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
问总共有多少条不同的路径？

示例 1:
输入: m = 3, n = 2
输出: 3
解释:
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向右 -> 向下
2. 向右 -> 向下 -> 向右
3. 向下 -> 向右 -> 向右

示例 2:
输入: m = 7, n = 3
输出: 28

提示：
1 <= m, n <= 100
题目数据保证答案小于等于 2 * 10 ^ 9

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-paths
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
        排列组合：C(m+n-1,m-1)
        :param m:
        :param n:
        :return:
        '''
        n,m=n+m-2,m-1
        S1=1
        for i in range(n,n-m,-1):
           S1*=i
        S2=1
        for i in range(1,m+1):
            S2*=i
        return S1//S2

    def uniquePaths2(self, m: int, n: int) -> int:
        '''
        动态规划 P(i,j)为到达(i,j)的最多路径走法
        P(i,j)=P(i-1,j)+P(i,j-1)
        :param m:
        :param n:
        :return:
        '''
        P=[[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            P[i][0]=1
        for j in range(n):
            P[0][j]=1

        for i in range(1,m):
            for j in range(1,n):
                P[i][j]=P[i-1][j]+P[i][j-1]

        return P[-1][-1]


if __name__ == '__main__':
    S=Solution()
    print(S.uniquePaths(4,7))
    print(S.uniquePaths2(4, 7))