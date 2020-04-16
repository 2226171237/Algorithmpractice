'''
如何判断字符串是否是整数？
写一个方法，判断字符串是否是整数，如果是整数，则返回其整数值。
'''

def isNumber(c):
    return  '0'<=c<='9'

# 方法1：递归法
def string2int1(s):
    sign=True if isNumber(s[0]) else False
    def toInt(s):
        if len(s)<=1:
            return ord(s)-ord('0')
        num=ord(s[-1])-ord('0')
        if 0<=num<=9:
            result=10*toInt(s[:-1])+num
            return result
        else:
            raise ValueError('not a number string')
    if sign:
        return toInt(s)
    else:
        return -toInt(s[1:])

# 方法2：非递归
def string2int2(s):
    sign = -1 if s[0]=='-' else 1
    result=0
    i=0 if isNumber(s[0]) else 1
    for x in s[i:]:
        if isNumber(x):
            result*=10
            result+=ord(x)-ord('0')
        else:
            raise ValueError('not a number string')
    return sign*result

if __name__ == '__main__':
    s='+12345'
    print(string2int1(s))
    print(string2int2(s))