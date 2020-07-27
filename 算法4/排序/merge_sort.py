from base_sort import BasicSort

class MergeSort(BasicSort):
    def sort1(self,arr):
        '''自顶向下是实现'''
        self.arr_aux=arr.copy()
        def _sort(arr,low,high):
            if low>=high:
                return
            mid=(low+high)//2
            _sort(arr,low,mid)
            _sort(arr,mid+1,high)
            return self.merge(arr,low,mid,high)
        _sort(arr,0,len(arr)-1)

    def merge(self,arr,low,mid,high):
        self.arr_aux[low:high+1]=arr[low:high+1]
        i=low
        j=mid+1
        for k in range(low,high+1):
            if i>mid:
                arr[k]=self.arr_aux[j]
                j+=1
            elif j>high:
                arr[k]=self.arr_aux[i]
                i+=1
            elif self.arr_aux[i]>self.arr_aux[j]:
                arr[k]=self.arr_aux[j]
                j+=1
            else:
                arr[k]=self.arr_aux[i]
                i+=1
    def sort(self,arr):
        '''
        自底向上实现,归并排序的非递归版本
        :param arr:
        :return:
        '''
        n=len(arr)
        self.arr_aux=arr.copy()
        size=1  # 代表子序的长度
        while size<n:
            i=0
            while i<n-1:
                self.merge(arr,i,i+size-1,min(i+size+size-1,n-1))
                i+=size*2
            size*=2

if __name__ == '__main__':
    s=MergeSort()
    s.check()

    # arr_cpy=[]
    # def merge(arr,low,mid,high):
    #     arr_cpy[low:high+1]=arr[low:high+1]
    #     i=low
    #     j=mid+1
    #     for k in range(low,high+1):
    #         if i>mid:
    #             arr[k]=arr_cpy[j]
    #             j+=1
    #         elif j>high:
    #             arr[k]=arr_cpy[i]
    #             i+=1
    #         elif arr_cpy[i]>arr_cpy[j]:
    #             arr[k]=arr_cpy[j]
    #             j+=1
    #         else:
    #             arr[k]=arr_cpy[i]
    #             i+=1
