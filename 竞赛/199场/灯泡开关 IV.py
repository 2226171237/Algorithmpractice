class Solution(object):
    def minFlips(self, target):
        """
        :type target: str
        :rtype: int
        """
        if len(target)==0:
            return 0
        cnt=0
        i=len(target)-1
        if target[i]=='1':
            cnt+=1
        i-=1
        while i>=0:
            if target[i]=='1' and target[i+1]=='0':
                cnt+=2
            i-=1
        return cnt
