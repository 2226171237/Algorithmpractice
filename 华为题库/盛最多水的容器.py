'''
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

示例：
输入：[1,8,6,2,5,4,8,3,7]
输出：49

说明：你不能倾斜容器，且 n 的值至少为 2。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/container-with-most-water
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def maxArea(self, height) -> int:
        '''
        参考，柱状图中最大矩形，暴力搜素,超时
        :param list[int] height:
        :return: int
        '''
        maxArea=0
        for i in range(len(height)):
            for j in range(i+1,len(height)):
                maxArea=max(maxArea,min(height[i],height[j])*(j-i))
        return maxArea

    def maxArea2(self, height) -> int:
        '''
        双指针法，
        :param list[int] height:
        :return: int
        '''
        left,right=0,len(height)-1
        maxArea=0
        while left<right:
            maxArea=max(maxArea,min(height[left],height[right])*(right-left))
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return maxArea




if __name__ == '__main__':
    S=Solution()
    print(S.maxArea([1,8,6,2,5,4,8,3,7]))
    print(S.maxArea2([1, 8, 6, 2, 5, 4, 8, 3, 7]))

