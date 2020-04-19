'''
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
示例:
输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6
'''
class Solution:
    def trap(self, height) -> int:
        '''
        暴力法，某一位置的雨水等于两边最大高度的较小值，减去当前高度。类似找函数左右最小的极值
        :param list[int] height:
        :return: int
        '''
        water=0
        for i in range(len(height)):
            leftmax=height[i]
            j=i-1
            while j>=0:
                if height[j]>leftmax and height[j]>height[i]:
                    leftmax=height[j]
                j-=1
            j=i+1
            rightmax=height[i]
            while j<len(height):
                if height[j]>rightmax and height[j]>height[i]:
                    rightmax=height[j]
                j+=1
            water+=min(leftmax,rightmax)-height[i]
        return water

    def trap2(self, height) -> int:
        '''
        改进暴力法，加入动态规划，找到坐标最大值，找到右边最大值
        :param list[int] height:
        :return: int
        '''
        water=0
        leftmax=[0 for _ in range(len(height))]
        rightmax=[0 for _ in range(len(height))]

        # 找每个数左边最大值，动态规划
        Max=0
        for i,x in enumerate(height):
            Max=max(x,Max)
            leftmax[i]=Max
        # 找每个数右边的最大值，动态规划
        Max=0
        i=len(height)-1
        while i>=0:
            Max=max(Max,height[i])
            rightmax[i]=Max
            i-=1
        for i in range(len(height)):
            water+=min(leftmax[i],rightmax[i])-height[i]
        return water


if __name__ == '__main__':
    S=Solution()
    print(S.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
    print(S.trap2([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))


