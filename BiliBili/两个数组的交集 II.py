'''
给定两个数组，编写一个函数来计算它们的交集。

示例 1：
输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2,2]
示例 2:
输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[4,9]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/intersection-of-two-arrays-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        D1=dict()
        for x in nums1:
            D1[x]=D1.get(x,0)+1
        res=[]
        D2=dict()
        for x in nums2:
            D2[x]=D2.get(x,0)+1
        for key in D1:
            if key in D2:
                res.extend([key for _ in range(min(D1[key],D2[key]))])
        return res
