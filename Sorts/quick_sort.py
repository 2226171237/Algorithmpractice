'''
快速排序
'''
def partition(X,low,high):
    base=X[low]
    while low<high:
        while low<high and base<=X[high]:
            high-=1
        X[low]=X[high]
        while low<high and base>X[low]:
            low+=1
        X[high]=X[low]
    X[low]=base
    return low

def qsort(X,low,high):
    if low>=high:
        return
    mid=partition(X,low,high)
    qsort(X,low,mid-1)
    qsort(X,mid+1,high)



if __name__ == '__main__':
    import random

    X = [random.randint(10, 30) for _ in range(40)]
    print(X)
    qsort(X,0,len(X)-1)
    print(X)