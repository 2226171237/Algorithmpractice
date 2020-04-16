'''
冒泡排序
'''

def bubble_sort(X):
    i=0
    n=len(X)
    while i<n-1:
        j=0
        while j<n-i-1:
            if X[j]>X[j+1]:
                t=X[j]
                X[j]=X[j+1]
                X[j+1]=t
            j+=1
        i+=1
    return X


if __name__ == '__main__':
    import random

    X = [random.randint(10, 30) for _ in range(40)]
    print(X)
    print(bubble_sort(X))