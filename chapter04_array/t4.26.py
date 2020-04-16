# -*-coding=utf-8 -*-
'''
磁盘分区
'''

# 判断N个磁盘(数组d)和M个分区(数组p)是否可以分配成功。
def is_allocable(d,p):
    d_index=0
    i=0
    while i<len(p):
        if d_index>=len(d):
            return False
        if d[d_index]>=p[i]:
            d[d_index]-=p[i]
            i+=1
        else:
            d_index+=1
    return True

if __name__ == '__main__':
    d=[120,120,120]
    p=[60,60,80,20,80]
    print(is_allocable(d,p))