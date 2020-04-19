'''
这里有 n 个航班，它们分别从 1 到 n 进行编号。
我们这儿有一份航班预订表，表中第 i 条预订记录 bookings[i] = [i, j, k] 意味着我们在从 i 到 j 的每个航班上预订了 k 个座位。
请你返回一个长度为 n 的数组 answer，按航班编号顺序返回每个航班上预订的座位数。

示例：
输入：bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
输出：[10,55,45,25,25]
 
提示：
1 <= bookings.length <= 20000
1 <= bookings[i][0] <= bookings[i][1] <= n <= 20000
1 <= bookings[i][2] <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/corporate-flight-bookings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def corpFlightBookings(self, bookings,n: int):
        '''
        超时
        :param list[list[int]] bookings:
        :param n:
        :return: list[int]
        '''
        result=[0 for _ in range(n)]

        for i,j,k in bookings:
            for m in range(i,j+1):
                result[m-1]+=k
        return result

    def corpFlightBookings2(self, bookings,n: int):
        '''
        超时
        :param list[list[int]] bookings:
        :param n:
        :return: list[int]
        '''
        result=[0 for _ in range(n)]
        hashmap=dict()
        for i,j,k in bookings:
            if (i,j) not in hashmap:
                hashmap[(i,j)]=k
            else:
                hashmap[(i,j)]+=k

        for i,j in hashmap:
            for m in range(i,j+1):
                result[m-1]+=hashmap[(i,j)]
        return result

    def corpFlightBookings3(self, bookings,n: int):
        '''

        :param list[list[int]] bookings:
        :param n:
        :return: list[int]
        '''
        result=[0 for _ in range(n)]
        for i,j,k in bookings:
            result[i-1]+=k  # 上了多少人
            if j<n:
                result[j]-=k # 下了多少人， 得到每个站的人数变化，即两站之间的差分
        for i in range(1,n):
            result[i]+=result[i-1]
        return result

if __name__ == '__main__':
    S=Solution()
    print(S.corpFlightBookings([[1,2,10],[2,3,20],[2,5,25]], n = 5))
    print(S.corpFlightBookings2([[1,2,10],[2,3,20],[2,5,25]], n = 5))
    print(S.corpFlightBookings3([[1, 2, 10], [2, 3, 20], [2, 5, 25]], n=5))