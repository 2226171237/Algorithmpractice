'''
给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。
你可以对一个单词进行如下三种操作：
插入一个字符
删除一个字符
替换一个字符

示例 1：
输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')

示例 2：
输入：word1 = "intention", word2 = "execution"
输出：5
解释：
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')
'''

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        '''
        动态规划 P[i,j]为word1[:i+1] 到word2[:j+1]的最少编辑数
        if word1[i]==word2[j]：p[i,j]=min(P[i-1,j-1],P[i-1,j]+1,P[i,j-1]+1)
        else: P[i,j]=min(P[i-1,j-1]+1,P[i-1,j]+1,P[i,j-1]+1)
        :param word1:
        :param word2:
        :return:
        '''
        if len(word1)==0:
            return len(word2)
        if len(word2)==0:
            return len(word1)
        m,n=len(word1),len(word2)
        P=[[0 for _ in range(n+1)] for _ in range(m+1)]
        i=0
        while i<m+1:
            P[i][0]=i
            i+=1
        i=0
        while i<n+1:
            P[0][i]=i
            i+=1
        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i-1]==word2[j-1]:
                    P[i][j]=min(P[i-1][j-1],P[i-1][j]+1,P[i][j-1]+1)  # 保留，删除，插入
                else:
                    P[i][j]=min(P[i-1][j-1]+1,P[i-1][j]+1,P[i][j-1]+1) # 替换，删除，插入 加的1相当于操作复杂度
        return P[m][n]



if __name__ == '__main__':
    word1='intention'
    word2='execution'
    S=Solution()
    print(S.minDistance(word1,word2))