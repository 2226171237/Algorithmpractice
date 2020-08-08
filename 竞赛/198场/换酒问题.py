class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        if numExchange>numBottles:
            return numBottles
        cnt=numBottles  # 一次喝完所有瓶
        while numBottles>=numExchange:
            cnt+=numBottles//numExchange  # 空瓶可以换的数量
            numBottles=numBottles//numExchange+numBottles%numExchange # 没喝的喝完+空瓶数量
        # cnt+=numBottles
        return cnt



if __name__ == '__main__':
    s=Solution()
    print(s.numWaterBottles(9,3))