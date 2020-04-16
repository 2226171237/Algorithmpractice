
class Solution:
    def __init__(self):
        self.bigHeap=[] # 大顶堆
        self.smallHeap=[] # 小顶堆
        self.nums=0

    def insertBigHeap(self,x):
        self.bigHeap.append(x)
        index=len(self.bigHeap)-1
        parent=index//2
        while parent>=0:
            if self.bigHeap[index]>self.bigHeap[parent]:
                self.bigHeap[index],self.bigHeap[parent]=self.bigHeap[parent],self.bigHeap[index]
                index=parent
                parent=index//2
            else:
                break
    def insertSmallHeap(self,x):
        self.smallHeap.append(x)
        index = len(self.smallHeap) - 1
        parent = index // 2
        while parent >= 0:
            if self.smallHeap[index] < self.smallHeap[parent]:
                self.smallHeap[index], self.smallHeap[parent] = self.smallHeap[parent], self.smallHeap[index]
                index = parent
                parent = index // 2
            else:
                break
    def bigHeapPop(self):  # 节点i 的子节点为2*i+1，2*i+2
        if len(self.bigHeap)==0:
            return None
        self.bigHeap[-1],self.bigHeap[0]=self.bigHeap[0],self.bigHeap[-1]
        t=self.bigHeap.pop()
        index=0
        child=2*index+1
        while child<len(self.bigHeap):
            if child+1<len(self.bigHeap) and self.bigHeap[child+1]>self.bigHeap[child]:
                child+=1
            if self.bigHeap[index]<self.bigHeap[child]:
                self.bigHeap[index],self.bigHeap[child]=self.bigHeap[child],self.bigHeap[index]
            else:
                break
        return t

    def smallHeapPop(self):
        if len(self.smallHeap)==0:
            return None
        self.smallHeap[-1],self.smallHeap[0]=self.smallHeap[0],self.smallHeap[-1]
        t=self.smallHeap.pop()
        index=0
        child=2*index+1
        while child<len(self.smallHeap):
            if child+1<len(self.smallHeap) and self.smallHeap[child+1]<self.smallHeap[child]:
                child+=1
            if self.smallHeap[index]>self.smallHeap[child]:
                self.smallHeap[index],self.smallHeap[child]=self.smallHeap[child],self.smallHeap[index]
            else:
                break
        return t

    def Insert(self, num):
        # write code here
        if self.nums&1==0:
            self.insertBigHeap(num)
            self.insertSmallHeap(self.bigHeapPop())
        else:
            self.insertSmallHeap(num)
            self.insertBigHeap(self.smallHeapPop())
        self.nums+=1

    def GetMedian(self):
        if self.nums&1==1:
            return self.smallHeap[0]
        else:
            return (self.smallHeap[0]+self.bigHeap[0])/2

# write code here

if __name__ == '__main__':
    L=[1,2,2,3,4,5,7,8,9,10,10]
    S=Solution()
    for x in L:
        S.Insert(x)
        print(S.GetMedian())
