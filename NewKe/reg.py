"""
牛牛有两个字符串A和B,其中A串是一个01串,B串中除了可能有0和1,还可能有'?',B中的'?'可以确定为0或者1。
寻找一个字符串T是否在字符串S中出现的过程,称为字符串匹配。牛牛现在考虑所有可能的字符串B,有多少种可
以在字符串A中完成匹配。

例如:A = "00010001", B = "??"
字符串B可能的字符串是"00","01","10","11",只有"11"没有出现在字符串A中,所以输出3
"""

class Solution:
    def is_match(self, A,B):
        i=0
        while i<len(A):
            if A[i]==B[i] or B[i]=='?':
                i+=1
            else:
                return False
        return True

    def match_num(self,A,B):
        a_len=len(A)
        b_len=len(B)
        i=0
        result=set()
        while i<a_len-b_len+1:
            t=A[i:i+b_len]
            if self.is_match(t,B):
                if t not in result:
                    result.add(t)
            i+=1
        return len(result)

if __name__ == '__main__':
    S=Solution()
    A='0100100111'
    B='?1?'
    print(S.match_num(A,B))
