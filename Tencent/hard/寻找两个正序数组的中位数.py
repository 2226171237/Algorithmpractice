'''
两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。
请你找出这两个正序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
你可以假设 nums1 和 nums2 不会同时为空。

示例 1:
nums1 = [1, 3]
nums2 = [2]
则中位数是 2.0
示例 2:
nums1 = [1, 2]
nums2 = [3, 4]
则中位数是 (2 + 3)/2 = 2.5
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/median-of-two-sorted-arrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

import heapq
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        无论奇偶都是遍历到 N//2+1
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        N=len(nums1)+len(nums2)
        mid=N//2
        prev=0
        cur=0
        i=0
        j=0
        for k in range(mid+1):
            prev=cur
            if i>=len(nums1):
                cur=nums2[j]
                j+=1
            elif j>=len(nums2):
                cur=nums1[i]
                i+=1
            elif nums1[i]<nums2[j]:
                cur=nums1[i]
                i+=1
            else:
                cur=nums2[j]
                j+=1
        return cur if N%2!=0 else (cur+prev)/2

if __name__ == '__main__':
    s=Solution()
    print(s.findMedianSortedArrays([1,2],[3,4]))
