'''
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
求在该柱状图中，能够勾勒出来的矩形的最大面积。

示例:
输入: [2,1,5,6,2,3]
输出: 10
'''
class Solution:
    def largestRectangleArea1(self, heights) -> int:
        '''
        暴力求解,求每两个柱子之间形成的最大矩形(必须包含之间所有柱子)
        :param list[int] heights:
        :return:
        '''
        maxArea=0
        for i in range(len(heights)):
            for j in range(i,len(heights)):
                maxArea=max(maxArea,min(heights[i:j+1])*(j-i+1))
        return maxArea

    def largestRectangleArea2(self, heights) -> int:
        '''
        暴力求解,优化，去掉求最小值
        :param list[int] heights:
        :return:
        '''
        maxArea=0
        for i in range(len(heights)):
            Mins=heights[i]
            for j in range(i,len(heights)):
                Mins=min(Mins,heights[j])
                maxArea=max(maxArea,Mins*(j-i+1))
        return maxArea
    def largestRectangleArea3(self, heights) -> int:
        '''
        分治
        :param list[int] heights:
        :return:
        '''
        maxArea=[0]
        def solve(begin,end):
            if begin>end:
                return
            elif begin==end:
                maxArea[0]=max(maxArea[0],heights[begin])
            else:
                minIndex=begin  # 找begin 到 end的最小高度
                for i in range(begin,end+1):
                    if heights[minIndex]>heights[i]:
                        minIndex=i
                maxArea[0]=max(maxArea[0],heights[minIndex]*(end-begin+1))
                solve(begin,minIndex-1)
                solve(minIndex+1,end)
        solve(0,len(heights)-1)
        return maxArea[0]

    def largestRectangleArea4(self, heights) -> int:
        # 堆栈
        Stack=[]
        maxArea=0
        for x in heights:
            if len(Stack)==0 or Stack[-1]<=x:
                Stack.append(x)
            else:
                i=1
                while len(Stack)!=0 and Stack[-1]>x:
                    maxArea=max(maxArea,Stack.pop()*i)
                    i+=1
        i = 1
        while len(Stack) != 0:
            maxArea = max(maxArea, Stack.pop() * i)
            i += 1
        return maxArea

if __name__ == '__main__':
    S=Solution()
    print(S.largestRectangleArea1([2,1,5,6,2,3]))
    print(S.largestRectangleArea2([2, 1, 5, 6, 2, 3]))
    print(S.largestRectangleArea3([2, 1, 5, 6, 2, 3]))
    print(S.largestRectangleArea4([2, 1, 5, 6, 2, 3]))



