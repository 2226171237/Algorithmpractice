'''
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:
输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
示例 2:
输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4
说明:
你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。
来源力扣（LeetCode）
链接：https://leetcode-cn.com/problems/kth-largest-element-in-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


def partition(arr,low,high):
    key=arr[low]
    while low<high:
        while low<high and arr[high]<key:
            high-=1
        arr[low]=arr[high]

        while low<high and arr[low]>=key:
            low+=1
        arr[high]=arr[low]
    arr[low]=key
    return low

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res=[0]
        def findK(arr,low,high,k):
            if low>high:
                return
            id=partition(arr,low,high)
            if id==k-1:
                res[0]=arr[id]
                return
            elif id<k-1:
                findK(arr,id+1,high,k)
            else:
                findK(arr,low,id-1,k)

        N=len(nums)
        if k<=0 or k>N:
            return -1
        findK(nums,0,N-1,k)
        return res[0]

if __name__ == '__main__':
    s=Solution()
    print(s.findKthLargest([3,2,1,5,6,4],2))
