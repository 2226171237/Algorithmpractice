

def shell_sort(arr):
    N=len(arr)
    h=N//2
    while h>=1:
        for i in range(h,N):
            for j in range(i,h-1,-h):
                if arr[j]<arr[j-h]:
                    arr[j],arr[j-h]=arr[j-h],arr[j]
                else:
                    break
        h//=2

if __name__ == '__main__':
    arr=[1,3,4,2,5,3,2,2,1]
    shell_sort(arr)
    print(arr)
