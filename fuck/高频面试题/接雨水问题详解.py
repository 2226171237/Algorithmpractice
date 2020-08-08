


def trap(heights):
    leftmax=[heights[0]]
    rightmax=[heights[-1]]
    i=1
    while i<len(heights):
        if heights[i]>leftmax[-1]:
            leftmax.append(heights[i])
        else:
            leftmax.append(leftmax[-1])
        i+=1
    i=len(heights)-1
    while i>=0:
        if heights[i]>rightmax[-1]:
            rightmax.append(heights[i])
        else:
            rightmax.append(rightmax[-1])
        i-=1
    ans=0
    for i in range(1,len(heights)-1):
        h=min(leftmax[i-1],rightmax[len(heights)-i-1])-heights[i]
        ans+=h
    return ans
