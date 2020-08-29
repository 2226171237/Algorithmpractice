'''
小明买了一些彩色的气球用绳子串在一条线上，想要装饰房间，每个气球都染上了一种颜色，每个气球的形状都是各不相同的。
我们用1到9一共9个数字表示不同的颜色，如12345则表示一串5个颜色各不相同的气球串。但小明希望得到不出现重复颜色的
气球串，那么现在小明需要将这个气球串剪成多个较短的气球串，小明一共有多少种剪法？如原气球串12345的一种是剪法是
剪成12和345两个气球串。

注意每种剪法需满足最后的子串中气球颜色各不相同（如果满足该条件，允许不剪，即保留原串）。
两种剪法不同当且仅当存在一个位置，在一种剪法里剪开了，而在另一种中没剪开。详见样例分析。
输入
第一行输入一个正整数n（1≤n≤100000），表示气球的数量。
第二行输入n个整数a1，a2，a3...an，ai表示该气球串上第i个气球的颜色。对于任意i，有1≤ai≤9。
样例输入
3
1 2 3

输出
输出一行，第一行输出一个整数，表示满足要求的剪法，输出最终结果除以1000000007后的余数。
样例输出
4
'''

import sys
def solve(nums):
    dp=[0 for _ in range(len(nums)+1)]
    dp[0]=1
    dp[1]=1
    for i in range(1,len(nums)):
        dums=[0 for _ in range(10)]
        for j in range(i,-1,-1):
            dums[nums[j]]+=1
            if dums[nums[j]]>1:
                break
            dp[i+1]+=dp[j]

    return dp[-1]% 1000000007

# n=int(sys.stdin.readline().strip())
# nums=[int(x) for x in sys.stdin.readline().strip().split()]
# print(solve(nums))
if __name__ == '__main__':
    print(solve([1,2,3]))