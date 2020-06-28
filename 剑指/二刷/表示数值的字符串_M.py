'''
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
例如，字符串"+100"、"5e2"、"-123"、"3.1416"、"0123"都表示数值，
但"12e"、"1a3.14"、"1.2.3"、"+-5"、"-1E-16"及"12e+5.4"都不是。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/biao-shi-shu-zhi-de-zi-fu-chuan-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution(object):
    def __init__(self):
        self.idx=0

    def scanUnsignedInt(self,s):
        while self.idx<len(s) and 0<=ord(s[self.idx])-ord('0')<=9:
            self.idx+=1

    def scanInter(self,s):
        if self.idx<len(s) and s[self.idx] in '+-':
            self.idx+=1
        self.scanUnsignedInt(s)

    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # A.BeC
        s=s.strip()
        if len(s)==0:
            return False
        self.idx=0
        self.scanInter(s) # A
        if self.idx<len(s) and s[self.idx]=='.': # 小数部分B
            self.idx+=1
            self.scanUnsignedInt(s)
        if 0<self.idx<len(s) and s[self.idx] in 'eE': # C部分
            self.idx+=1
            begin = self.idx
            self.scanInter(s)
            if self.idx==begin:
                return False
        return self.idx==len(s)

    def isNumber2(self,s):
        '''状态机'''
        state={0:{'+':1,'-':1,' ':0,'num':2,'.':7},
               1:{'num':2,'.':7},
               2:{'num':2,'e':4,'E':4,'.':3,' ':8},
               3:{'num':3,'e':4,'E':4,' ':8},
               4:{'num':5,'+':6,'-':6},
               5:{'num':5,' ':8},
               6:{'num':5},
               7:{'num':3},
               8:{' ':8}}
        finish_state=[2,3,5,8]
        current_state=0
        for x in s:
            x='num' if 0<=ord(x)-ord('0')<=9 else x
            if x in state[current_state]:
                current_state=state[current_state][x]
            else:
                return False
        if current_state in finish_state:
            return True
        else:
            return False

if __name__ == '__main__':
    s=Solution()
    print(s.isNumber('01e1'))
    print(s.isNumber2('1 '))
