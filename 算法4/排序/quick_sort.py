from base_sort import BasicSort

class QuickSort(BasicSort):
    def partition(self,arr,low,high):
        key=arr[low]
        while low<high:
            while low<high and key<arr[high]:
                high-=1
            arr[low]=arr[high]
            while low<high and key>=arr[low]:
                low+=1
            arr[high]=arr[low]
        arr[low]=key
        return low

    def sort(self,arr):
        def _sort(arr,low,high):
            if high<=low:
                return
            mid=self.partition(arr,low,high)
            _sort(arr,low,mid-1)
            _sort(arr,mid+1,high)
        _sort(arr,0,len(arr)-1)

    def sort2(self,arr):
        '''
        三向切分实现
        :param arr:
        :return:
        '''
        def _sort(arr,low,high):
            if low>=high:
                return
            lt=low
            gt=high
            i=low+1
            v=arr[low]
            while i<=gt:
                if arr[i]>v:
                    self.swap(arr,i,gt)
                    gt-=1
                elif arr[i]<v:
                    self.swap(arr,i,lt)
                    lt+=1
                    i+=1
                else:
                    i+=1
            _sort(arr,low,lt-1)
            _sort(arr,gt+1,high)
        _sort(arr,0,len(arr)-1)

if __name__ == '__main__':
    import random,time
    s=QuickSort()
    x=[3,4,1,2,5]
    s.sort(x)
    print(x)
    s.check()

    x1=[random.randint(0,1) for _ in range(10000)]
    x2=x1.copy()
    start=time.perf_counter()
    s.sort2(x)
    print(time.perf_counter()-start)
    start = time.perf_counter()
    s.sort(x)
    print(time.perf_counter()-start)

    import pickle
    from glob import  glob
    file=glob('./*.py')
    print(file)
    with open('test.pkl','wb') as f:
        pickle.dump({1:12,2:13,3:14},f)
    with open('test.pkl', 'rb') as f:
        data=pickle.load(f)
    print(data)