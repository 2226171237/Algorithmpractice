'''
编写一个算法来判断一个数 n 是不是快乐数。
「快乐数」定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，
然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。如果 可以变为  1，那么这个数就是快乐数。
如果 n 是快乐数就返回 True ；不是，则返回 False 。

示例：
输入：19
输出：true
解释：
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/happy-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def getNext(self,n):
        s=0
        while n:
            s+=(n%10)**2
            n=n//10
        return s

    def isHappy(self, n: int) -> bool:
        '''
        哈希表
        :param n:
        :return:
        '''
        hashset=set()
        while n!=1:
            n=self.getNext(n)
            if n not in hashset:
                hashset.add(n)
            else:
                return False
        return True

    def isHappy2(self,n:int)->bool:
        '''
        检查连边是否存在环，快慢指针法
        :param n:
        :return:
        '''
        slow=self.getNext(n)
        fast=self.getNext(self.getNext(n))
        while fast!=1 and slow!=fast:
            slow=self.getNext(slow)
            fast=self.getNext(self.getNext(fast))
        return fast==1

if __name__ == '__main__':
    S=Solution()
    print(S.isHappy(19))
    print(S.isHappy2(19))