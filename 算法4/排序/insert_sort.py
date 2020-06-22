
from base_sort import BasicSort

class InsertSort(BasicSort):
    def sort(self,arr):
        n=len(arr)
        for i in range(1,n):
            for j in range(i,0,-1):
                if arr[j]<arr[j-1]:
                    self.swap(arr,j,j-1)

if __name__ == '__main__':
    s=InsertSort()
    s.check()
