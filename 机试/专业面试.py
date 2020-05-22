'''
给定一个字符串s和一个字符串p,请问至少去掉s中的多少个字符，才能使得p是s的子串？

输入：
两行，第一行为字符串s,第二行为字符串p,(s和p只包含小写英文字字母，s的长度不超过2000，p的长度不超过10，且保证有解)
输出：
最少去掉的字符个数。

实例：
输入:
axb
ab
输出：
1
'''
class Solution:
    def getLeastCnt(self,s:str,p:str)->int:
        if len(p)==0:
            return 0
        if len(s)==0:
            return -1
        m,n=len(s),len(p)
        P=[[0 for _ in range(n)] for _ in range(m)]

        ishave =p[0] in s
        i=0
        while i<m:
            P[i][0]=0 if ishave else -1
            i+=1
        i=1
        while i<n:
            P[0][i]=-1
            i+=1

        for i in range(1,m):
            for j in range(1,n):
                if s[i]==p[j]:
                    a=P[i-1][j-1]  # 保留s_i
                    if a==-1:
                        P[i][j]=-1
                    else:
                        # 找到S(i-1) 以P(j-1)结束要至少删除多少个字符
                        k=0
                        ii=i-1
                        jj=j-1
                        while jj>=0 and ii>=0:
                            if s[ii]==p[jj]:
                                ii-=1
                                jj-=1
                            else:
                                k+=1
                                ii-=1
                        P[i][j]=k if jj<0 else -1

                    b=P[i-1][j]+1 if P[i-1][j]!=-1 else -1 # 删除s_i
                    if b!=-1:
                        P[i][j]=b if P[i][j]==-1 else min(P[i][j],b)
                else:
                    P[i][j]=P[i-1][j]+1 if P[i-1][j]!=-1 else -1
        for p in P:
            print(p)
        return P[-1][-1]

if __name__ == '__main__':
    S=Solution()
    print(S.getLeastCnt('xbxc','bc'))