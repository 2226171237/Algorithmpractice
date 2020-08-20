

class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        tmp=[]
        for x in s:
            if len(tmp)==0:
                tmp.append(x)
            elif abs(ord(tmp[-1])-ord(x))==ord('a')-ord('A'):
                tmp.pop()
            else:
                tmp.append(x)
        return ''.join(tmp)


if __name__ == '__main__':
    s=Solution()
    print(s.makeGood('LeEeetcode'))