

def sublen(string,a):
    i=len(string)-1
    cnt=0
    while i>=0:
        if string[i]==a:
            cnt+=1
        else:
            break
        i-=1
    return cnt

class Solution(object):
    def getLengthOfOptimalCompression(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        rows=len(s)
        cols=k+1
        P=[[0 for _ in range(cols)] for _ in range(rows)]
        strings=[['' for _ in range(cols)] for _ in range(rows)]
        P[0][0]=1
        strings[0][0]=s[0]
        for k in range(1,cols):
            P[0][k]=0
            strings[0][k]=''
        nums=1
        for i in range(1,rows):
            strings[i][0]=s[:i+1]
            if s[i]==s[i-1]:
                nums+=1
                P[i][0]=P[i-nums+1][0]+len(str(nums))
            else:
                nums=1
                P[i][0]=P[i-1][0]+1
        for k in range(1,cols):
            for i in range(1,rows):
                L=sublen(strings[i-1][k],s[i])
                if L==0 or L==1 or L==9 or L==99:
                    A=P[i-1][k]+1
                else:
                    A=P[i-1][k]

                if A<P[i-1][k-1]:
                    P[i][k]=A
                    strings[i][k]=strings[i-1][k]+s[i]
                else:
                    P[i][k]=P[i-1][k-1]
                    strings[i][k]=strings[i-1][k-1]
        for p in P:
            print(p)
        return P[-1][-1]

if __name__ == '__main__':
    s=Solution()
    print(s.getLengthOfOptimalCompression('aaabcccd',2))