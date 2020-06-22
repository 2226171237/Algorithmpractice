# -*- coding:utf-8 -*-

# 所有的排序基类
import random
class BasicSort(object):
    def swap(self,arr,i,j):
        arr[i],arr[j]=arr[j],arr[i]

    def compare(self,a,b):
        return a<=b

    def sort(self,arr):
        raise NotImplementedError

    def isSorted(self,arr):
        if len(arr)<=1:
            return True

        for i in range(1,len(arr)):
            if self.compare(arr[i-1],arr[i]):
                continue
            else:
                return False
        return True

    def check(self):
        SIZE,BATCH=1024,200
        cnt=1.
        for _ in range(BATCH):
            arr=[random.random() for _ in range(random.randint(100,SIZE))]
            self.sort(arr)
            if not self.isSorted(arr):
                print("test error in %% %f。" %  (100.*cnt/BATCH))
                return
            cnt+=1
        print('test succesed 100%')

