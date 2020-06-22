'''
在数组中的两个数字，如果前面一个数字大于后面的数字，
则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。
'''
class Solution(object):
    def __init__(self):
        self.aux=[]
    def reversePairs(self, nums):
        """
        归并排序实现
        :type nums: List[int]
        :rtype: int
        """
        size=1
        N=len(nums)
        cnt=0
        self.aux=nums.copy()
        while size<N:
            i=0
            while i<N-1:
                cnt+=self.merge(nums,i,i+size-1,min(i+size+size-1,N-1))
                i+=size*2
            size*=2
        return cnt

    def merge2(self, nums, low, mid, high):
        if low >= high:
            return 0
        cnt = 0
        for i in range(low, mid + 1):
            for j in range(mid + 1, high + 1):
                if nums[i] > nums[j]:
                    cnt += 1
        return cnt

    def merge(self,nums,low,mid,high):
        self.aux[low:high+1]=nums[low:high+1]
        cnt=0
        i=low
        j=mid+1
        for k in range(low,high+1):
            if i>mid:
                nums[k]=self.aux[j]
                j+=1
            elif j>high:
                # cnt+=high-mid 下面条件已经加了，否则会重复
                nums[k]=self.aux[i]
                i+=1
            elif self.aux[i]>self.aux[j]:
                cnt+=mid-i+1
                nums[k]=self.aux[j]
                j+=1
            else:
                nums[k] = self.aux[i]
                i+=1
        return cnt

if __name__ == '__main__':
    import random
    s=Solution()
    random.seed(42)
    x=[random.randint(0,100) for _ in range(50000)]
    print(s.reversePairs(x))