'''
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
求在该柱状图中，能够勾勒出来的矩形的最大面积。
'''

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack=[-1]
        maxA=0
        heights.append(0)
        for i in range(len(heights)):
            while len(stack)>1 and heights[stack[-1]]>heights[i]:
                h=heights[stack[-1]]
                stack.pop()
                maxA=max(h*(i-stack[-1]-1),maxA)
            stack.append(i)
        heights.pop()
        return maxA

if __name__ == '__main__':
    s=Solution()
    print(s.largestRectangleArea([2,1,5,6,2,3]))