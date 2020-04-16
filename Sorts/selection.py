'''
选择第k小的元素
'''
def partition(arr,low,high):
    base=arr[low]
    while low<high:
        while low<high and base<=arr[high]:
            high-=1
        arr[low]=arr[high]
        while low<high and base>arr[low]:
            low+=1
        arr[high]=arr[low]
    arr[low]=base
    return low

def selection(X,k):
    # 选择最k小的数
    if k<1 or k>len(X):
        raise ValueError('the value of k is too small or too bigger!')

    def select(X,low,high,k):
        if low>=high:
            return high
        mid=partition(X,low,high)
        t=mid-low+1
        if t>=k:
            return select(X,low,mid,k)
        else:
            return select(X,mid+1,high,k-t)

    return select(X,0,len(X)-1,k)


if __name__ == '__main__':
    import random
    X=[1,2,3,4,5,6,7]
    random.shuffle(X)
    print(X)
    print(X[selection(X,6)])