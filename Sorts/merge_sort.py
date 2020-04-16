'''
归并排序
'''

def merge_sort(X,low,high):
    if low>high:
        return []
    if low==high:
        return [X[low]]

    # 拆分
    mid=(low+high)//2
    A=merge_sort(X,low,mid)
    B=merge_sort(X,mid+1,high)
    # 合并
    result=[]
    i=0
    j=0
    while i<len(A) and j<len(B):
        if A[i]<B[j]:
            result.append(A[i])
            i+=1
        else:
            result.append(B[j])
            j+=1
    if i<len(A):
        result.extend(A[i:])
    if j<len(B):
        result.extend(B[j:])
    return result

if __name__ == '__main__':
    import random

    X = [random.randint(10, 30) for _ in range(40)]
    print(X)
    print(merge_sort(X,0,len(X)-1))
