# -*- coding:utf-8 -*-

# 大顶堆

class MaxPQ:
    def __init__(self):
        self._size=0
        self._data=[0] # 第一个元素不使用

    def is_empty(self):
        return self._size==0

    @property
    def size(self):
        return self._size

    def insert(self,x):
        self._data.append(x)
        self._size += 1
        current_idx=self._size
        parent_idx=current_idx//2
        while parent_idx>=1 and self._data[current_idx]>self._data[parent_idx]:
            self._data[parent_idx],self._data[current_idx]=self._data[current_idx],self._data[parent_idx]
            current_idx=parent_idx
            parent_idx=current_idx//2

    def delMax(self):
        if self.is_empty():
            return None
        res=self._data[1]
        self._data[1]=self._data[-1]
        self._data.pop()
        self._size -= 1
        current_idx=1
        child_idx=2*current_idx
        while child_idx<=self._size:
            if child_idx+1<=self._size and self._data[child_idx+1]>self._data[child_idx]:
                child_idx=child_idx+1
            if self._data[current_idx]<self._data[child_idx]:
                self._data[current_idx],self._data[child_idx]=self._data[child_idx],self._data[current_idx]
                current_idx=child_idx
                child_idx=2*current_idx
            else:
                break
        return res


# 堆排序实现，使用从右到左用下沉的方法构造子堆
from base_sort import BasicSort
class HeapSort(BasicSort):

    def down(self,arr,i,N):
        current_idx = i
        child_idx = current_idx *2
        while child_idx <= N:
            if child_idx + 1 <= N and arr[child_idx - 1] < arr[child_idx]:
                child_idx = child_idx + 1
            if arr[child_idx - 1] > arr[current_idx - 1]:
                arr[current_idx - 1], arr[child_idx - 1] = arr[child_idx - 1], arr[current_idx - 1]
                current_idx=child_idx
                child_idx=current_idx*2
            else:
                break

    def sort(self,arr):
        N=len(arr)
        for i in range(N//2,0,-1):
            # 下沉
            self.down(arr,i,N)

        for i in range(N,0,-1):
            # 将当前最大元素添加到数组末尾
            arr[0],arr[i-1]=arr[i-1],arr[0]
            # 堆根结点进行下沉
            self.down(arr,1,i-1)

if __name__ == '__main__':
    maxHeap=MaxPQ()
    maxHeap.insert(2)
    maxHeap.insert(4)
    maxHeap.insert(1)
    maxHeap.insert(0)
    maxHeap.insert(5)
    maxHeap.insert(2)
    print([maxHeap.delMax() for _ in range(6)])
    s=HeapSort()
    x=[3,2,4,5,1,0,6]
    s.sort(x)
    print(x)
    s.check()


