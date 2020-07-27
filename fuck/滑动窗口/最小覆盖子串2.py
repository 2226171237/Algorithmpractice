
class Solution(object):
    def minWindow(self, s, t):
        N=len(s)
        windows=dict()
        needs=dict()
        for x in t:
            needs[x]=needs.get(x,0)+1
        need_matchs=len(needs)
        matchs=0
        left,right=0,0
        minLen=2**31
        while right<N:
            c=s[right]
            if c in needs:
                windows[c]=windows.get(c,0)+1
                if windows[c]==needs[c]:
                    matchs+=1
            while matchs==need_matchs and left<right:
                minLen=min(minLen,right-left+1)
                c=s[left]
                if c in needs:
                    windows[c]-=1
                    if windows[c]<needs[c]:
                        matchs-=1
                left+=1
            right+=1
        return minLen
