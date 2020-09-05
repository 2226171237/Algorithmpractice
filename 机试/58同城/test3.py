
class Solution:
    def translateNum(self , num ):
        # write code here
        num=str(num)
        N=len(num)
        if N==0:
            return 0
        if N==1:
            return 1 if num[0]>'0' else 0
        first=1
        second=1
        i=1
        while i<N:
            t=second
            if num[i]=='0':
                if (num[i-1]=='1' or num[i-1]=='2'):
                    second=second+first
                else:
                    second=first
            else:
                if num[i-1]=='1' or (num[i-1]=='2' and '1'<=num[i]<='5'):
                    second=second+first
            first=t
            i+=1
        return second

if __name__ == '__main__':
    s=Solution()
    print(s.translateNum(12158))
