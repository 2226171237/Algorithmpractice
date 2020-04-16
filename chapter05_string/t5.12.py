'''
如何判断一个字符串是否包含重复字符
'''

def isDup1(s):
    d=set()
    for x in s:
        if x not in d:
            d.add(x)
        else:
            return True
    return False

def isDup2(s):
    flags=[0 for _ in range(256)]
    for x in s:
        if flags[ord(x)]==0:
            flags[ord(x)]=1
        else:
            return True
    return False
if __name__ == '__main__':
    s='abcdefgd4'
    print(isDup1(s))
    print(isDup2(s))