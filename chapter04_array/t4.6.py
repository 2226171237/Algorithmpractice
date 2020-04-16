#-*-coding=utf-8-*-
'''
如何找出数组中第k小的数。
给定一个整数数组，如何快速求出数组中第k小的数，加入数组为[4,0,1,0,2,3],
则第3小的元素是1.
'''
# 排序法
def findMin_K1(arr,k):
    return sorted(arr)[k-1]

# 部分排序法(选择排序，排到前k个就停止)
def findMin_K2(arr,k):

    i=0
    while i<k:
        j=i+1
        while j<len(arr):
            if arr[i]>arr[j]:
                tmp=arr[i]
                arr[i]=arr[j]
                arr[j]=tmp
            j+=1
        i+=1
    return arr[k-1]

# 类快速排序方法
def findMin_K3(arr,left_num,k):

    provit=arr[0]
    left=[x for x in arr[1:] if x<provit]
    if len(left)+left_num==k-1:
        return provit
    elif len(left)+left_num>k-1:
        return findMin_K3(left,left_num,k)
    else:
        right=[x for x in arr[1:] if x>=provit]
        return findMin_K3(right,left_num+len(left)+1,k)

# 引申：在O(N)时间复杂度内查找数组中前三名。
# 类选择排序方法
def find_top_K1(arr,k):
    i = 0
    while i < k:
        j = i + 1
        while j < len(arr):
            if arr[i] < arr[j]:
                tmp = arr[i]
                arr[i] = arr[j]
                arr[j] = tmp
            j += 1
        i += 1
    return arr[0:k]

def find_top_K2(arr,k):
    top_k=[-2**31 for _ in range(k)]
    for x in arr:
        for i,y in enumerate(top_k):
            if x>y:
                j=k-1
                while j>i:
                    top_k[j]=top_k[j-1]
                    j-=1
                top_k[i]=x
                break
    return top_k

if __name__ == '__main__':
    arr=[4,0,1,0,2,3]
    print(findMin_K1(arr,6))
    print(findMin_K2(arr, 6))
    print(findMin_K3(arr,0, 6))
    print(find_top_K1(arr,4))
    print(find_top_K2(arr, 4))
