'''
你的面前有一堵方形的、由多行砖块组成的砖墙。 这些砖块高度相同但是宽度不同。你现在要画一条自顶向下的、穿过最少砖块的垂线。
砖墙由行的列表表示。 每一行都是一个代表从左至右每块砖的宽度的整数列表。

如果你画的线只是从砖块的边缘经过，就不算穿过这块砖。你需要找出怎样画才能使这条线穿过的砖块数量最少，并且返回穿过的砖块数量。
你不能沿着墙的两个垂直边缘之一画线，这样显然是没有穿过一块砖的。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/brick-wall
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def leastBricks(self, wall) -> int:
        '''
        差分,超时了
        :param list[list[int]] wall:
        :return:
        '''
        H=len(wall)
        Wall=[[] for _ in range(H)]
        for i,onelayer in enumerate(wall):
            k=1
            for w in onelayer:
                while w:
                    Wall[i].append(k)
                    w-=1
                k+=1
        if len(Wall[0])==1:
            return H
        # 每行差分,# 每列求1的个数
        CrossNums = [0 for _ in range(len(Wall[0])-1)]
        for i in range(H):
            for j in range(len(Wall[0])-1):
                Wall[i][j]=Wall[i][j+1]-Wall[i][j]
                CrossNums[j]+=Wall[i][j]
        return H-max(CrossNums)

    def leastBricks2(self, wall) -> int:
        '''
        哈希表
        :param wall:
        :return:
        '''
        hashmap=dict()
        for onelayer in wall:
            sum=0
            for w in onelayer[:-1]:
                sum+=w
                if sum in hashmap:
                    hashmap[sum]+=1
                else:
                    hashmap[sum]=1
        if not hashmap:
            return len(wall)
        return len(wall)-max(hashmap.values())

if __name__ == '__main__':
    S=Solution()
    wall= [[1,2,2,1],
           [3,1,2],
           [1,3,2],
           [2,4],
           [3,1,2],
           [1,3,1,1]]
    print(S.leastBricks2([[1],[1],[1]]))

