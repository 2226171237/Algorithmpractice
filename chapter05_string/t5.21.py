# -*- coding:utf-8 -*-
'''
如何截取包含中文的字符串？
编写一个截取字符串的函数，输入为一个字符串和字节数，输出为按字节截取的字符串。但是要
保证汉字不能截半个，例如'人ABC'4，应该截为'人AB'。

encoding=utf-8 一个中文占3个字节，unicode 中，占2个
'''


def isChinese(c):
    return True if c>=u'\u4e00' and c<=u'\u9fa5' else False

def splitStr(s,bs):
    i=0
    n=len(s)
    sb=''
    b=0
    while i<n:
        if isChinese(s[i]):
            if b+2>bs:
                break
            else:
                sb+=s[i]
                b+=2
        else:
            if b+1>bs:
                break
            else:
                sb+=s[i]
                b+=1
        i+=1
    return sb


if __name__ == '__main__':
    s='人ABCD们'  # python3中str就是Unicode编码
    print(s.encode())
    print(splitStr(s,7))