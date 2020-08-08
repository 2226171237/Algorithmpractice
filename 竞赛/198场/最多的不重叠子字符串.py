
from functools import  cmp_to_key
from collections import Counter
def compare(a,b):
    if a[-1]==b[-1]:
        if a[-1]-b[-1]>0:
            return 1
        else:
            return -1
    elif a[-1]>b[-1]:
        return 1
    else:
        return -1

class Solution(object):
    def maxNumOfSubstrings(self, s):
        """
        区间合并
        :type s: str
        :rtype: List[str]
        """
        lines = []
        for i in range(len(s)):
            s2 = set(s[i])
            for j in range(i, len(s)):
                s2.add(s[j])
                if s2 & set(s[0:i] + s[j + 1:]):
                    continue
                else:
                    lines.append([i, j])

        lines=sorted(lines,key=cmp_to_key(compare))
        res=[]
        res.append(lines[0])
        i=1
        while i<len(lines):
            if lines[i][0]>res[-1][-1]:
                res.append(lines[i])
            i+=1
        substrings=[s[a:b+1] for a,b in res]
        return substrings

if __name__ == '__main__':
    s=Solution()
    print(s.maxNumOfSubstrings("abab"))
