'''
如何判断一个字符串是否由另外一个字符串旋转得到。
给定一个能判断一个单词是否为另一个单词的子字符串的方法isSubstring。如何判断s2是否能通过旋转s1得到
(只能使用一次isSubstring).
'''
def isSubstring(s1,s2):
    # s2是否是s1的子串
    i=0
    j=0
    n1=len(s1)
    n2=len(s2)
    while i<n1-n2:
        j=0
        while j<n2 and s1[i+j]==s2[j]:
            j+=1
        if j==n2:
            return True
        else:
            j=0
        i+=1
    return False

def isRoated(s1,s2):
    s=s1+s1
    if isSubstring(s,s2):
        return True
    else:
        return False

if __name__ == '__main__':
    s1='waterbottle'
    s2='ttlewaterbe'
    print(isRoated(s1,s2))
