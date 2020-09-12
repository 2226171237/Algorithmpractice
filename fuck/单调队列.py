
# 找k大小的滑窗内的最大值

from collections import deque
def getMaxValueOfWindows(nums,k):
    result=[]
    Q=deque()
    for i in range(k):
        while len(Q) and nums[Q[-1]]<=nums[i]:
            Q.pop()
        Q.append(i)
    result.append(nums[Q[0]])
    for i in range(k,len(nums)):
        while len(Q) and nums[Q[-1]]<=nums[i]:
            Q.pop()
        Q.append(i)
        while len(Q) and i-Q[0]>=k:
            Q.popleft()
        result.append(nums[Q[0]])
    return result


print(getMaxValueOfWindows([1,3,-1,-3,5,3,6,7],3))