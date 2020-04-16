'''
堆排序
'''

def swap(X,i,j):
    t=X[i]
    X[i]=X[j]
    X[j]=t

def build_heap(X):
    # 建立大顶堆
    i=1
    n=len(X)
    while i<n:
        j=i
        while j:
            p=j//2
            if X[p]<X[j]:
                swap(X,j,p)
                j=p
            else:
                break
        i+=1


def rearrange_heap(X,n):
    i=0
    if 2*i+1<n:
        child = 2 * i if X[2 * i] > X[2 * i + 1] else 2 * i + 1
    else:
        child=2*i
    while child<n:
        if X[child]>X[i]:
            swap(X,i,child)
            i=child
            if 2 * i + 1 < n:
                child = 2 * i if X[2 * i] > X[2 * i + 1] else 2 * i + 1
            else:
                child = 2 * i
        else:
            break

def headp_sort(X):
    # 建立初始堆
    build_heap(X)
    i=0
    n=len(X)
    while i<n-1:
        swap(X,0,n-i-1)
        rearrange_heap(X,n-i-1)
        i+=1

if __name__ == '__main__':

    import random
    X = [random.randint(10, 30) for _ in range(40)]
    print(X)
    headp_sort(X)
    print(X)

