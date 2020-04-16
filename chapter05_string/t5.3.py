'''
如何对字符串进行反转
'''
# 方法1：直接交换
def reversedStr1(s,end=''):
    s=list(s)
    i=0
    j=len(s)-1
    while i<j:
        t=s[i]
        s[i]=s[j]
        s[j]=t
        i+=1
        j-=1
    return end.join(s)

# 方法2：异或法交换
def reversedStr2(s):
    s=list(s)
    i=0
    j=len(s)-1
    while i<j:
        s[i]=str(ord(s[i])^ord(s[j]))
        s[j]=str(ord(s[i])^ord(s[j]))
        s[i]=str(ord(s[i])^ord(s[j]))
        i+=1
        j-=1
    return ''.join(s)

# 引申：如何实现单词反转
def reversedWords(s):
    s=reversedStr1(s)
    s=reversedStr1(s.split(),end=' ')
    return s
if __name__ == '__main__':
    s='hello world'
    print(reversedStr1(s))
    print(reversedStr1(s))
    print(reversedWords('hello world'))