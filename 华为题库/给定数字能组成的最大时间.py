'''
给定一个由 4 位数字组成的数组，返回可以设置的符合 24 小时制的最大时间。
最小的 24 小时制时间是 00:00，而最大的是 23:59。从 00:00 （午夜）开始算起，过得越久，时间越大。
以长度为 5 的字符串返回答案。如果不能确定有效时间，则返回空字符串。

示例 1：
输入：[1,2,3,4]
输出："23:41"

示例 2：
输入：[5,5,5,5]
输出：""
 
提示：
A.length == 4
0 <= A[i] <= 9

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/largest-time-for-given-digits
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def __init__(self):
        self.maxTime=[]
    def largestTimeFromDigits(self, A) -> str:
        '''
        穷举
        :param list[int] A:
        :return:
        '''
        def _permuite(A,i,time:list):
            if i==len(A):
                if ((time[0]==2 and time[1]<=3) or (time[0]<=1)) and time[2]<=5:
                    if self.maxTime==[]:
                        self.maxTime=time.copy()
                    else:
                        for k in range(4):
                            if time[k]==self.maxTime[k]:
                                continue
                            elif time[k]<self.maxTime[k]:
                                break
                            else:
                                self.maxTime=time.copy()
                                break
                return
            for j in range(i,len(A)):
                A[i],A[j]=A[j],A[i]
                time.append(A[i])
                _permuite(A,i+1,time)
                time.pop()
                A[i], A[j] = A[j], A[i]

        _permuite(A,0,[])
        if len(self.maxTime)==0:
            return ''
        return "{}{}:{}{}".format(*self.maxTime)

if __name__ == '__main__':
    S=Solution()
    print(S.largestTimeFromDigits([0,4,0,0]))