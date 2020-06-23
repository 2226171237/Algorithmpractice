'''
输入整数数组 arr ，找出其中最小的 k 个数。
例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。

示例 1：
输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]

示例 2：
输入：arr = [0,1,2,1], k = 1
输出：[0]
 
限制：
0 <= k <= arr.length <= 10000
0 <= arr[i] <= 10000
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

def partition(arr,low,high):
    key=arr[low]
    while low<high:
        while low<high and arr[high]>key:
            high-=1
        arr[low]=arr[high]
        while low<high and arr[low]<=key:
            low+=1
        arr[high]=arr[low]
    arr[low]=key
    return low

class Solution(object):
    def getLeastNumbers(self, arr, k):
        """
        快排
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        result=[]
        def getKMins(arr, low, high, k):
            if low > high:
                return 
            mid=partition(arr,low,high)
            if mid<k:
                result.extend(arr[low:mid+1])
                getKMins(arr, mid + 1, high, k)
            elif mid==k:
                result.extend(arr[low:mid])
                return
            else:
                getKMins(arr,low,mid-1,k)

        getKMins(arr,0,len(arr)-1,k)
        return result

if __name__ == '__main__':
    s=Solution()
    print(s.getLeastNumbers([4,5,1,6,2,7,3,8],4))

