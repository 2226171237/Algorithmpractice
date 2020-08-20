'''
给定二维空间中四点的坐标，返回四点是否可以构造一个正方形。
一个点的坐标（x，y）由一个有两个整数的整数数组表示。

示例:
输入: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
输出: True
注意:
所有输入整数都在 [-10000，10000] 范围内。
一个有效的正方形有四个等长的正长和四个等角（90度角）。
输入点没有顺序。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-square
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

from functools import cmp_to_key
def compare(p1,p2):
    if p1[0]>p2[0]:
        return 1
    elif p1[0]==p2[0]:
        return 1 if p1[1]>p2[1] else -1
    return -1

def distance(p1,p2):
    return (p1[0]-p2[0])**2+(p1[1]-p2[1])**2

def center(p1,p2):
    return [p1[0]+p2[0],p1[1]+p2[1]]

def dot(p1,p2):
    return p1[0]*p2[0]+p1[1]*p2[1]

class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        points=[p1,p2,p3,p4]
        maxL1,maxL2=0,0
        maxVec=[[0,0],[0,0]]
        for i in range(3):
            for j in range(i+1,4):
                d=distance(points[i],points[j])
                if d>maxL1:
                    maxL2=maxL1
                    maxL1=d
                    maxVec[1]=maxVec[0]
                    maxVec[0]=[i,j]
                elif d>maxL2:
                    maxL2=d
                    maxVec[1]=[i,j]
        if maxL1!=maxL2 or maxL1==0:
            return False
        c1=center(points[maxVec[0][0]],points[maxVec[0][1]])
        c2 = center(points[maxVec[1][0]], points[maxVec[1][1]])
        if c1[0]!=c2[0] or c1[1]!=c2[1]:
            return False
        vec1=[points[maxVec[0][0]][0]-points[maxVec[0][1]][0],points[maxVec[0][0]][1]-points[maxVec[0][1]][1]]
        vec2 = [points[maxVec[1][0]][0] - points[maxVec[1][1]][0], points[maxVec[1][0]][1] - points[maxVec[1][1]][1]]
        if 0!=dot(vec1,vec2):
            return False
        return True

    def validSquare2(self, p1, p2, p3, p4):
        p1,p2,p3,p4=sorted([p1,p2,p3,p4],key=cmp_to_key(compare))
        vec1=[p4[0]-p1[0],p4[1]-p1[1]]
        vec2=[p3[0]-p2[0],p3[1]-p2[1]]
        if 0!=dot(vec1,vec2) or distance(p1,p4)==0:
            return False
        c1=center(p1,p4)
        c2=center(p2,p3)
        if c1[0]!=c2[0] or c1[1]!=c2[1]:
            return False
        return True

    def validSquare3(self, p1, p2, p3, p4):
        '''把六条线长度平方算出来，如果有4条是相等的，且剩余两条是这四条的两倍，'''
        d1=distance(p1,p2)
        d2=distance(p1,p3)
        d3=distance(p1,p4)
        d4=distance(p2,p3)
        d5=distance(p2,p4)
        d6=distance(p3,p4)
        d=sorted([d1,d2,d3,d4,d5,d6])
        return d[0]!=0 and d[0]==d[1]==d[2]==d[3] and d[4]==d[5] and d[4]==2*d[0]

if __name__ == '__main__':
    s=Solution()
    print(s.validSquare(p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]))
    print(s.validSquare2(p1=[0, 0], p2=[1, 1], p3=[1, 0], p4=[0, 1]))


