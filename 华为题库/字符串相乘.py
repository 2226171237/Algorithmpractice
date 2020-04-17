'''
给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

示例 1:
输入: num1 = "2", num2 = "3"
输出: "6"

示例 2:
输入: num1 = "123", num2 = "456"
输出: "56088"

说明：
num1 和 num2 的长度小于110。
num1 和 num2 只包含数字 0-9。
num1 和 num2 均不以零开头，除非是数字 0 本身。
不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/multiply-strings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def add(self,num1:str,num2:str):
        # index=0 为个位
        result=[]
        i=0
        S,C=0,0
        while i<len(num1) and i<len(num2):
            S=ord(num1[i])+ord(num2[i])-2*ord('0')+C
            if S>=10:
                S-=10
                C=1
            else:
                C=0
            result.append(str(S))
            i+=1
        num=num1 if i<len(num1) else num2
        while i<len(num):
            S = ord(num[i]) - ord('0') + C
            if S>=10:
                S-=10
                C=1
            else:
                C=0
            result.append(str(S))
            i+=1
        if C==1:
            result.append('1')
        return ''.join(result)

    def multiply(self, num1: str, num2: str) -> str:
        # 模拟乘法
        result='0'
        for i,n in enumerate(num2[::-1]):
            res='0'
            for _ in range(int(n)):
                res=self.add(num1[::-1],res)
            res='0'*i+res # 左移
            result=self.add(res,result)
        return result[::-1]

    def multiply2(self,num1:str,num2:str)->str:
        # 优化竖式  num1[i]*num2[j]=[result[i+j],result[i+j+1]]
        n1,n2=len(num1),len(num2)
        result=[0 for _ in range(n1+n2)]
        i=n1-1
        while i>=0:
            j=n2-1
            while j>=0:
                t=(ord(num1[i])-ord('0'))*(ord(num2[j])-ord('0'))
                S,C=(t+result[i+j+1])%10,(t+result[i+j+1])//10
                result[i+j+1]=S
                result[i+j]+=C  # 自然而然下次会处理，加和大于十的情况
                j-=1
            i-=1
        prod=''
        for i,x in enumerate(result):
            if x==0:
                prod=''.join(list(map(str,result[i+1:])))
                break
        return prod








if __name__ == '__main__':
    import time
    S=Solution()
    start=time.time()
    print(S.multiply('1232131214123213121412321312', '123213121412321312141232131214123'))
    print(time.time()-start)
    start = time.time()
    print(S.multiply2('1232131214123213121412321312', '123213121412321312141232131214123'))
    print(time.time() - start)