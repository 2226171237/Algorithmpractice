'''
如何求字符串里最长回文子串。
'''

# 中心扩展法
def expander(s,c1,c2):
    n=len(s)
    while c1>=0 and c1<n and s[c1]==s[c2]:
        c1-=1
        c2+=1
    return c1+1,(c2-1)-(c1+1)+1

def getLongestPalindrome1(s):
    n=len(s)
    i=0
    maxLen=0
    while i<n-1:
        c1,len1=expander(s,i,i)
        if len1>maxLen:
            maxLen=len1
            index=c1
        c1,len1=expander(s,i,i+1)
        if len1>maxLen:
            maxLen=len1
            index=c1
        i+=1
    return s[index:index+maxLen]

# Manacher算法
def getLongestPalindrome2(s):
    pass

if __name__ == '__main__':
    print(getLongestPalindrome1('abcdefgfedxyz'))