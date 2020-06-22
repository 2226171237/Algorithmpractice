
from base_sort import BasicSort

class ShellSort(BasicSort):
    '''
    希尔排序
    '''
    def sort(self,arr):
        n=len(arr)
        h=1
        while h<n/3:
            h=3*h+1
        while h>=1:
            for i in range(h,n):
                for j in range(i,0,-h):
                    if arr[j]<arr[j-h]:
                        self.swap(arr,j,j-h)
            h//=3

if __name__ == '__main__':
    s=ShellSort()
    s.check()
