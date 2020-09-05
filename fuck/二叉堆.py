

class minHeap:
    '''小顶堆'''
    def __init__(self):
        self._data=[0]
        self._size=0

    def heapfily(self,items):
        self._data.extend(items)
        self._size=len(items)
        for i in range(self._size//2,0,-1):
            self.down(i)

    def down(self,idx):
        '''下沉'''
        cur=idx
        child=2*idx
        while child<=self._size:
            if child+1<=self._size and self._data[child+1]<self._data[child]:
                child=child+1
            if self._data[child]<self._data[cur]:
                self._data[child],self._data[cur]=self._data[cur],self._data[child]
                cur=child
                child=2*cur
            else:
                break

    def swim(self,idx):
        '''上浮'''
        cur=idx
        parent=idx//2
        while cur>1:
            if self._data[parent]>self._data[cur]:
                self._data[parent],self._data[cur]=self._data[cur],self._data[parent]
                cur=parent
                parent=cur//2
            else:
                break

    def heappush(self,x):
        self._data.append(x)
        self._size+=1
        self.swim(self._size)

    def heappop(self):
        ret=self._data[1]
        self._data[1]=self._data[self._size]
        self._data.pop()
        self._size-=1
        self.down(1)
        return ret


if __name__ == '__main__':
    heap=minHeap()
    heap.heapfily([3,2,1,4,5,7,0])
    print(heap.heappop())
    print(heap.heappop())
    print(heap.heappop())
    print(heap.heappop())
    print(heap.heappop())
    heap.heappush(12)
    heap.heappush(6)
    print(heap.heappop())
    print(heap.heappop())
    print(heap.heappop())
    print(heap.heappop())