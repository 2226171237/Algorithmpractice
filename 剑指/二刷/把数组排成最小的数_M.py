'''
输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。

示例 1:
输入: [10,2]
输出: "102"
'''

def compare(x1,x2):
    n1=int(str(x1)+str(x2))
    n2=int(str(x2)+str(x1))
    if n1>n2:
        return 1
    else:
        return -1

from functools import  cmp_to_key

def sort(arr):
    h=1
    while h<len(arr)/3:
        h=3*h+1
    while h>=1:
        for i in range(h,len(arr)):
            for j in range(i,0,-h):
                if compare(arr[j-h],arr[j])>0:
                    arr[j],arr[j-h]=arr[j-h],arr[j]
        h//=3

class Solution:


    def minNumber(self, nums):
        '''
        :type nums: List[int]
        :rtype : str
        '''
        #nums=sorted(nums,key=cmp_to_key(compare))
        sort(nums)
        print(nums)
        nums=[str(x) for x in nums]
        return ''.join(nums)


if __name__ == '__main__':
    s=Solution()
    print(s.minNumber([3,30,34,5,9]))