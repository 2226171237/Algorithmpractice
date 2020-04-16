'''
如何求字符串的编辑距离。
编辑距离又叫Levenshtein距离，是指两个字符串之间由一个转成另一个所需的最少编辑操作次数。
许可的编辑操作包括一个字符替换成另一个字符，插入一个字符，删除一个字符。请设计并实现一个算法
来计算两个字符串的编辑距离。假设替换的复杂度是删除与插入的两倍，该如何调整？
'''
def levenshtein(s1,s2,n):
    n1=len(s1)
    n2=len(s2)
    M=[[0 for _ in range(n2+1)] for _ in range(n1+1)]
    i=0
    j=0
    while i<n1+1:
        M[i][0]=i
        i+=1
    while j<n2+1:
        M[0][j]=j
        j+=1
    i=1
    while i<n1+1:
        j = 1
        while j<n2+1:
            if s1[i-1]==s2[j-1]:
                M[i][j]=min(M[i-1][j],M[i-1][j-1],M[i][j-1])
            else:
                M[i][j]=min(M[i-1][j]+1,M[i-1][j-1]+n,M[i][j-1]+1)
            j+=1
        i+=1
    return M[-1][-1]

if __name__ == '__main__':
    s1='bciln'
    s2='fciling'
    print(levenshtein(s1,s2,1))
    print(levenshtein(s1, s2, 2))