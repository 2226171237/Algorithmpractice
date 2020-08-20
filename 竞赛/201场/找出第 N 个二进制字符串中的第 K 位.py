


def invert(s):
    for i in range(len(s)):
        s[i]='1' if s[i]=='0' else '0'

def reverse(s):
    low=0
    high=len(s)-1
    while low<high:
        s[low],s[high]=s[high],s[low]
        low+=1
        high-=1

class Solution(object):
    def findKthBit(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        s=['0']
        for _ in range(n):
            t=s.copy()
            t.append('1')
            invert(s)
            reverse(s)
            s=t+s
        return s[k-1]


if __name__ == '__main__':
    s=Solution()
    print(s.findKthBit(2,3))

