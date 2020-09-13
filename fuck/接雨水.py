

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        leftmax=[height[0]]
        for x in height[1:]:
            if x>leftmax[-1]:
                leftmax.append(x)
            else:
                leftmax.append(leftmax[-1])
        rightmax=[height[-1]]
        for x in height[-2::-1]:
            if x>rightmax[-1]:
                rightmax.append(x)
            else:
                rightmax.append(rightmax[-1])
        res=0
        n=len(height)
        for i in range(n):
            water=min(leftmax[i],rightmax[n-i-1])-height[i]
            res+=water
        return res

s=Solution()
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))