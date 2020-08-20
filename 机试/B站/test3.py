class Solution:
    def GetCoinCount(self , N ):
        # write code here
        def _minCount(N):
            DP=[0 for _ in range(1025)]
            DP[1],DP[2],DP[3]=1,2,3
            if N<=3:
                return DP[N]
            for i in range(4,N+1):
                coin1=DP[i-1]
                coin4=DP[i-4] if i-4>=0 else 2**31
                coin16=DP[i-16] if i-16>=0 else 2**31
                coin64=DP[i-64] if i-64>=0 else 2**31
                DP[i]=min(coin1,coin4,coin16,coin64)+1
            return DP[N]
        return _minCount(1024-N)

if __name__ == '__main__':
    s=Solution()
    print(s.GetCoinCount(200))