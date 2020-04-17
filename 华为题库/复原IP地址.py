'''
给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。

示例:
输入: "25525511135"
输出: ["255.255.11.135", "255.255.111.35"]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/restore-ip-addresses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def restoreIpAddresses(self, s: str):
        '''
        回溯
        :param str s:
        :return: list[str]
        '''
        result=[]

        def recoverIp(s:str,i:int,subIP:list,dot_num:int):
            if i>len(s) or dot_num>3:
                return
            if i==len(s) and dot_num==3:
                result.append(''.join(subIP))
            oneNum=0
            for j in range(i,min(i+3,len(s))):
                oneNum=oneNum*10+ord(s[j])-ord('0')
                if oneNum>255:
                    break
                if len(subIP)==0:
                    subIP.append(str(oneNum))
                    recoverIp(s, j + 1, subIP, dot_num)
                    subIP.pop()
                else:
                    subIP.append('.')
                    subIP.append(str(oneNum))
                    recoverIp(s,j+1,subIP,dot_num+1)
                    subIP.pop()
                    subIP.pop()
                if oneNum==0:
                    break
        recoverIp(s,0,[],0)
        return result

if __name__ == '__main__':
    S=Solution()
    print(S.restoreIpAddresses('0100210'))
