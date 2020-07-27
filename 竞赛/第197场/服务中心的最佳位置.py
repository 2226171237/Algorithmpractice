'''
一家快递公司希望在新城市建立新的服务中心。公司统计了该城市所有客户在二维地图上的坐标，
并希望能够以此为依据为新的服务中心选址：使服务中心 到所有客户的欧几里得距离的总和最小 。

给你一个数组 positions ，其中 positions[i] = [xi, yi] 表示第 i 个客户在二维地图上的位置，
返回到所有客户的 欧几里得距离的最小总和 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-position-for-a-service-centre
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def getMinDistSum(self, positions):
        """
        凸函数三分套三分
        :type positions: List[List[int]]
        :rtype: float
        """
        def dis(x,y):
            return sum([((x_i-x)**2+(y_i-y)**2)**0.5 for x_i,y_i in positions])

        def three_divide(l,r,f,eps=1e-5):
            while r-l>eps:
                m=l+(r-l)/3
                mm=r-(r-l)/3
                if f(m)<f(mm):
                    r=mm
                else:
                    l=m
            return (l+r)/2

        lmin,rmax=0,100
        def  xf(mx):
            def yf(my): return dis(mx,my)
            return dis(mx,three_divide(lmin,rmax,yf))
        x=three_divide(lmin,rmax,xf)
        y=three_divide(lmin,rmax,lambda my:dis(x,my))
        return dis(x,y)


if __name__ == '__main__':
    s=Solution()
    print(s.getMinDistSum( [[0,1],[1,0],[1,2],[2,1]]))