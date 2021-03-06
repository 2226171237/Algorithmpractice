# -*-coding=utf-8 -*-
'''
如何按照要求构造新的数组？
给定一个数组a[N],希望构造一个新的数组b[N],其中 b[i]=a[0]*a[1]*...*a[N-1]/a[i]。
在构造数组过程中，有如下几点要求：
1：不允许使用除法；
2：要求O(1)空间复杂度和O(N)时间复杂度；
3：除遍历计数器与a[N],b[N]外，不可以使用新的变量(包含栈临时变量，堆空间和全局静态变量等)
4：请用程序实现并简单描述。
'''

def getArr(a):
    b=[1]
    n=len(a)
    i=1
    while i<n:
        b.append(b[i-1]*a[i-1])
        i+=1
    i=n-2
    while i>0:
        b[0]*=a[i+1]
        b[i]*=b[0]
        i-=1
    b[0]*=a[1]
    return b

if __name__ == '__main__':
    a=[1,2,3,4,5,6,7,8,9,10]
    print(getArr(a))