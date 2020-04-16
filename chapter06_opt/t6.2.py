'''
如何判断一个数是否为2的n次幂
'''

# 构造法
def isPower(n):
    if n<1:
        return False
    i=1
    while i>=n:
        if i==n:
            return True
        i<<=1
    return False

# 与操作
def isPower2(n):
    if n<1:
        return False
    m=n&(n-1)
    return m==0

if __name__ == '__main__':
    print(isPower(3))