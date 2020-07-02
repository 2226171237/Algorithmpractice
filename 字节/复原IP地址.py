'''
给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。
有效的 IP 地址正好由四个整数（每个整数位于 0 到 255 之间组成），整数之间用 '.' 分隔。

示例:
输入: "25525511135"
输出: ["255.255.11.135", "255.255.111.35"]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/restore-ip-addresses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):

    def isValid(self,s,i,j):
        if j-i+1>3:       # 'xxxx,xxxxx,xxxxxx,...'
            return False
        nums=int(s[i:j+1])
        if nums>255:          # '256'
            return False
        if s[i]=='0' and nums>0: # '0xx'
            return False
        if nums==0 and j-i+1>1: # '00','000'
            return False
        return True

    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res=[]
        N=len(s)

        for i in range(0,N-3):
            if not self.isValid(s,0,i):
                break
            for j in range(i+1,N-2):
                if not self.isValid(s,i+1,j):
                    break
                for k in range(j+1,N-1):
                    if not self.isValid(s,j+1,k):
                        break
                    else:
                        if self.isValid(s,k+1,N-1):
                            ip=[s[0:i+1],s[i+1:j+1],s[j+1:k+1],s[k+1:]]
                            res.append('.'.join(ip))
        return res

if __name__ == '__main__':
    s=Solution()
    print(s.restoreIpAddresses('010010'))

