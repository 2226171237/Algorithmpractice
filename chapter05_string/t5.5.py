'''
如何判断两个字符串的包含关系？
给定有字幕组成的字符串s1,s2，其中，s2的字母的个数少于s1,如何判断s1是否包含s2?
即出现在s2中的字符，s1中都存在。
'''

def isContion(sa,sb):
    s1=sa if len(sa)>len(sb) else sb
    s2=sb if len(sa)>len(sb) else sa
    hash_s=set()
    for s in s1:
        if s not in hash_s:
            hash_s.add(s)
    for s in s2:
        if s not in hash_s:
            return False
    return True

if __name__ == '__main__':
    s1='abcdef'
    s2='abc'
    print(isContion(s2,s1))
