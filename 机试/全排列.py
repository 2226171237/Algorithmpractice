

def getOne(arr):
    j=len(arr)-1
    i=j-1
    while i>=0:
        if arr[i]<arr[j]:
            return i
        i-=1
        j-=1
    return -1

def getTwo(arr,i):
    sel_index=i+1
    j=i+1
    while j<len(arr):
        if arr[j]>arr[i] and arr[j]<=arr[sel_index]:
            sel_index=j
        j+=1
    return sel_index

def reverse(arr,i,j):
    while i<j:
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j-=1

def permutation(arr):
    result=[]
    arr=sorted(list(arr))
    result.append(''.join(arr))
    while True:
        i=getOne(arr)
        if i<0:
            break
        j=getTwo(arr,i)
        arr[i],arr[j]=arr[j],arr[i]
        reverse(arr,i+1,len(arr)-1)
        result.append(''.join(arr))
    return result

if __name__ == '__main__':
    print(permutation('abc'))