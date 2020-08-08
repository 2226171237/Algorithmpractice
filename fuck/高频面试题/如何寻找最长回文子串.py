
# 中心扩展法

def palindrome(s,l,r):
    while l>=0 and r<len(s):
        if s[l]==s[r]:
            l-=1
            r+=1
        else:
            break
    return r-l-1

def longestPalindrome(s):
    maxLen=1
    for i in range(len(s)):
        maxLen=max(maxLen,palindrome(s,i,i))
        maxLen = max(maxLen, palindrome(s, i, i)+1)
    return maxLen
