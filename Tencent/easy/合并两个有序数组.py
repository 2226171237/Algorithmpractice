'''
给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。

说明:
初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。

示例:
输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3
输出: [1,2,2,3,5,6]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m-1,-1,-1):
            nums1[i+n]=nums1[i]
        i=n
        j=0
        for k in range(m+n):
            if i>=m+n:
                nums1[k]=nums2[j]
                j+=1
            elif j>=n:
                nums1[k]=nums1[i]
                i+=1
            elif nums1[i]>nums2[j]:
                nums1[k]=nums2[j]
                j+=1
            else:
                nums1[k]=nums1[i]
                i+=1


if __name__ == '__main__':
    s=Solution()
    num1=[1,2,4,5,6,0]
    num2=[5]
    s.merge(num1,5,num2,1)
    print(num1)