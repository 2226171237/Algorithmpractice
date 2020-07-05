'''

'''

from collections import deque

def remove(left:deque,right:deque,n):
    for i in range(len(left)):
        left[i]+=0.5
    for i in range(len(right)):
        right[i]-=0.5
    if left[-1]==n:
        left.pop()
    if right[0]==0:
        right.popleft()
    if left and right and left[-1]==right[0]:
        r_ant=right.popleft()
        l_ant=left.pop()
        left.append(r_ant)
        right.appendleft(l_ant)

class Solution(object):
    def getLastMoment(self, n, left, right):
        """
        超时
        :type n: int
        :type left: List[int]
        :type right: List[int]
        :rtype: int
        """
        if n==1:
            return 0
        leftQ=deque()  # 左边的蚂蚁
        for x in sorted(right):
            leftQ.append(x)
        rightQ=deque() # 右边的蚂蚁
        for x in sorted(left):
            rightQ.append(x)
        T = 0
        if leftQ and leftQ[-1]==n:
            leftQ.pop()
        if rightQ and rightQ[0]==0:
            rightQ.popleft()
        while rightQ and leftQ:
            remove(leftQ,rightQ,n)
            T+=0.5

        if leftQ:
            T+=n-leftQ[0]
        if rightQ:
            T+=rightQ[-1]
        return int(T)

    def getLastMoment2(self, n, left, right):
        if n==1:
            return 0
        leftQ=deque()  # 左边的蚂蚁
        for x in sorted(right):
            leftQ.append(x)
        rightQ=deque() # 右边的蚂蚁
        for x in sorted(left):
            rightQ.append(x)
        T = 0
        leftT=0
        rightT=0

        if leftQ and leftQ[-1]==n:
            leftQ.pop()
        if rightQ and rightQ[0]==0:
            rightQ.popleft()

        if leftQ and rightQ and leftQ[-1]+leftT==rightQ[0]+rightT:
            r_ant = rightQ.popleft()
            r_ant+=rightT-leftT
            l_ant = leftQ.pop()
            l_ant+=leftT-rightT
            leftQ.append(r_ant)
            rightQ.appendleft(l_ant)

        while rightQ and leftQ:
            if leftQ[0]+leftT >= rightQ[-1]+rightT:
                T+= max(n - (leftQ[0]+leftT), (rightQ[-1])+rightT)
                return int(T)
            else:
                red=(rightQ[0]+rightT)-(leftQ[-1]+leftT)
                red=0.5 if red<=1.5 else red//2
                T+=red
                leftT+=red
                # for i in range(len(leftQ)):
                #     leftQ[i] += red
                rightT-=red
                # for i in range(len(rightQ)):
                #     rightQ[i] -= red
                if leftQ[-1]+leftT == n:
                    leftQ.pop()
                if rightQ[0]+rightT == 0:
                    rightQ.popleft()
                if leftQ and rightQ and leftQ[-1]+leftT == rightQ[0]+rightT:
                    r_ant = rightQ.popleft()
                    r_ant+=rightT-leftT
                    l_ant = leftQ.pop()
                    l_ant+=leftT-rightT
                    leftQ.append(r_ant)
                    rightQ.appendleft(l_ant)

        if leftQ:
            T+=n-(leftQ[0]+leftT)
        if rightQ:
            T+=rightQ[-1]+rightT
        return int(T)

if __name__ == '__main__':
    s=Solution()
    print(s.getLastMoment(7,[],[0,1,2,3,4,5,6,7]))
    print(s.getLastMoment2(4,[4,3],[0,1]))