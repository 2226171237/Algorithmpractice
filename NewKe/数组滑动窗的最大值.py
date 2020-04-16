# -*- coding:utf-8 -*-
# 双端队列
from _collections import deque

class Solution:
    def maxInWindows(self, num, size):
        # write code here
        q,res=deque(),[]
        i=0
        while size>0 and i<len(num):
            if len(q)>0 and i-size+1>q[0]: # q[0] 已不再窗内
                q.popleft()
            while len(q)>0 and num[q[-1]]<num[i]: # 将小于当前值的元素从队列中弹出
                q.pop()
            q.append(i)
            if i>=size-1:
                res.append(num[q[0]])
            i+=1
        return res

if __name__ == '__main__':
    S=Solution()
    print(S.maxInWindows([2,3,4,2,6,5,2,1],3))
