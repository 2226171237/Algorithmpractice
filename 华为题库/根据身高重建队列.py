'''
假设有打乱顺序的一群人站成一个队列。 每个人由一个整数对(h, k)表示，
其中h是这个人的身高，k是排在这个人前面且身高大于或等于h的人数。
编写一个算法来重建这个队列。

注意：
总人数少于1100人。

示例
输入:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

输出:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/queue-reconstruction-by-height
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

from functools import cmp_to_key

def compare(L1:list,L2:list):
    if L1[0]>L2[0]:
        return 1
    elif L1[0]<L2[0]:
        return -1
    else:
        if L1[1]<L2[1]:
            return 1
        elif L1[1]>L2[1]:
            return -1
        else:
            return 0

class Solution:
    def reconstructQueue(self, people):
        '''
        先按照身高h为主，k为辐排序;h升序，k降序
        :param list[list[int]] people:
        :return: list[list[int]]
        '''
        people=sorted(people,key=cmp_to_key(compare))
        i=len(people)-1
        while i>=0:
            if people[i][1]>0:# 向后移动k个
                k=people[i][1]
                t=people[i]
                for j in range(k):
                    people[i+j]=people[i+j+1]
                people[i+k]=t
            i-=1
        return people


if __name__ == '__main__':
    S=Solution()
    print(S.reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]))
