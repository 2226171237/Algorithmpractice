from base_sort import BasicSort

class SelectSort(BasicSort):
    def sort(self,arr):
        n=len(arr)
        for i in range(n-1):
            min_i=i
            for j in range(i+1,n):
                if arr[min_i]>arr[j]:
                    min_i=j
            self.swap(arr,i,min_i)



if __name__ == '__main__':
    sort=SelectSort()
    sort.check()

