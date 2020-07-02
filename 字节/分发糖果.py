'''
老师想给孩子们分发糖果，有 N 个孩子站成了一条直线，老师会根据每个孩子的表现，预先给他们评分。
你需要按照以下要求，帮助老师给这些孩子分发糖果：

每个孩子至少分配到 1 个糖果。
相邻的孩子中，评分高的孩子必须获得更多的糖果。
那么这样下来，老师至少需要准备多少颗糖果呢？

示例 1:
输入: [1,0,2]
输出: 5
解释: 你可以分别给这三个孩子分发 2、1、2 颗糖果。
示例 2:
输入: [1,2,2]
输出: 4
解释: 你可以分别给这三个孩子分发 1、2、1 颗糖果。
     第三个孩子只得到 1 颗糖果，这已满足上述两个条件。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/candy
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def candy(self, ratings):
        """
        正反遍历
        :type ratings: List[int]
        :rtype: int
        """
        N=len(ratings)
        if 0==N:
            return 0
        candy=[1 for _ in range(N)]
        i=1
        while i<N:
            if ratings[i]>ratings[i-1]:
                candy[i]=candy[i-1]+1
            else:
                candy[i]=1
            i+=1

        # 反向调整
        i=N-2
        while i>=0:
            if ratings[i]>ratings[i+1] and candy[i]<=candy[i+1]: # 要保证正反都是对的
                candy[i]=candy[i+1]+1
            i-=1
        return sum(candy)

if __name__ == '__main__':
    s=Solution()
    print(s.candy([1,3,4,5,2]))

