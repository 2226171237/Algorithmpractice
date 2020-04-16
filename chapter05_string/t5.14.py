'''
如何统计字符串中连续的重复字符个数？
用递归的方法实现一个字符串中连续出现相同字符的最大值，如 'aaabbcc'中连续出现字符 'a'的最大值为3.
'abbc' 连续出现字符'b'的最大值2
'''

def getMaxDupChar(s):
    if len(s)<=1:
        return len(s)
    j=1
    while j<len(s) and s[0]==s[j]:
        j+=1
    next_j=getMaxDupChar(s[j:])
    if j>next_j:
        return j
    else:
        return next_j


if __name__ == '__main__':
    s='abbcdeeeeefg'
    print(getMaxDupChar(s))