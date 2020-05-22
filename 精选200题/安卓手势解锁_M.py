'''
我们都知道安卓有个手势解锁的界面，是一个 3 x 3 的点所绘制出来的网格。
给你两个整数，分别为 ​​m 和 n，其中 1 ≤ m ≤ n ≤ 9，那么请你统计一下有多少种解锁手势,
是至少需要经过 m 个点，但是最多经过不超过 n 个点的。

先来了解下什么是一个有效的安卓解锁手势:
    1.每一个解锁手势必须至少经过 m 个点、最多经过 n 个点。
    2.解锁手势里不能设置经过重复的点。
    3.假如手势中有两个点是顺序经过的，那么这两个点的手势轨迹之间是绝对不能跨过任何未被经过的点。
    4.经过点的顺序不同则表示为不同的解锁手势。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/android-unlock-patterns
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def __init__(self):
        self.used=[False for _ in range(9)]
        self.nums=0

    def isValid(self,i,last):
        if self.used[i]: # 已经访问过
            return False
        if last==-1: # 第一个访问点
            return True
        if (last+i)&1==1: # 是日字型，或相邻
            return True
        mid=(last+i)//2
        if mid==4:
            return self.used[mid]
        if last%3!=i%3 and last//3!=i//3: # 对角相邻
            return True
        return self.used[mid]

    def dfs(self,last,m,n,Len):
        if m<=Len<=n:
            self.nums+=1
        if Len>=n:
            return
        for i in range(9):
            if self.isValid(i,last):
                self.used[i]=True
                self.dfs(i,m,n,Len+1)
                self.used[i]=False

    def numberOfPatterns(self, m: int, n: int) -> int:
        self.nums=0
        self.dfs(-1,m,n,0)
        return self.nums



S=Solution()
print(S.numberOfPatterns(1,2))