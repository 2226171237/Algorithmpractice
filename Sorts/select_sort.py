'''
选择排序
'''

def getMax(arr):
    i=0
    m=0
    maxs=arr[0]
    while i<len(arr):
        if maxs<arr[i]:
            maxs=arr[i]
            m=i
        i+=1
    return m

def select_sort1(X):
    i=len(X)-1
    while i>0:
        j=getMax(X[:i+1])
        t=X[i]
        X[i]=X[j]
        X[j]=t
        i-=1
    return X

def select_sort2(X):
    i=0
    n=len(X)
    while i<n-1:
        j=i+1
        while j<n:
            if X[i]>X[j]:
                t=X[i]
                X[i]=X[j]
                X[j]=t
            j+=1
        i+=1
    return X

if __name__ == '__main__':
    import random

    X = [random.randint(10, 30) for _ in range(40)]
    print(X)
    print(select_sort1(X))
    print(select_sort2(X))