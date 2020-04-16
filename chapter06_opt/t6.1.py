'''
如何判断一个自然数是否是某个数的平方？
设计一个算法，判断给定的一个数n，是否是某一个数的平方，不能使用开方运算。
'''

# 二分法
def getNum1(n):
    if n<=1:
        return n
    low=0
    high=n
    while high-low>1:
        mid=(low+high)//2
        t=mid**2-n
        if t<0:
            low=mid
        elif t>0:
            high=mid
        else:
            return mid
    return -1

def getNum2(n):
    i=1
    while True:
        n=n-i
        if n>0:
            i+=2
        elif n==0:
            return True
        else:
            return False
        
if __name__ == '__main__':
    for i in range(1,50):
        print(i,getNum1(i),getNum2(i))