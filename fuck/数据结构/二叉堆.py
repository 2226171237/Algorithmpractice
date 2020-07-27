
class MyPQ:
    def __init__(self,arr=None):
        self._data=[0]
        self._size=0
        if arr:
            self._heapfily(arr)

    def is_empty(self):
        return self._size==0

    def _heapfily(self,arr):
        self._data.extend(arr)
        self._size+=len(arr)
        for i in range(self._size//2,0,-1):
            self.sink(i)

    def swim(self,i):
        cur=i
        par=cur//2
        while par>0:
            if self._data[cur]<self._data[par]:
                self._data[cur],self._data[par]=self._data[par],self._data[cur]
                cur=par
                par=cur//2
            else:
                break

    def sink(self,i):
        cur=i
        child=2*cur
        while child<=self._size:
            if child+1<=self._size and self._data[child+1]<self._data[child]:
                child=child+1
            if self._data[cur]>self._data[child]:
                self._data[cur],self._data[child]=self._data[child],self._data[cur]
                cur=child
                child=cur*2
            else:
                break

    def append(self,x):
        self._data.append(x)
        self._size+=1
        self.swim(self._size)

    def pop(self):
        if self.is_empty():
            raise ValueError
        t=self._data[1]
        self._data[1]=self._data[-1]
        self._data.pop()
        self._size-=1
        self.sink(1)
        return t


if __name__ == '__main__':
    arr = [3, 2, 4,3,4,5,6,1,2,9]
    PQ=MyPQ(arr)
    while not PQ.is_empty():
        print(PQ.pop(),end=' ')
    print()
