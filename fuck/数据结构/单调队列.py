# 找滑动窗口内的最大值
from collections import deque
def getMax(nums,k):
    Q=deque()
    result=[]
    for i in range(len(nums)):
        # 维护单减队列
        while len(Q) and nums[Q[0]]<nums[i]:
            Q.pop()
        Q.append(i)
        if i>=k-1:
            while len(Q) and i-Q[0]+1>k: # 越界调整
                Q.popleft()
            result.append(nums[Q[0]])  # 对首就是最大值
    return result

print(getMax([1,3,-1,-3,5,3,2,1,0],3))
