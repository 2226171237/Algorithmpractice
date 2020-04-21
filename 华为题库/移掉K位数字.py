'''
给定一个以字符串表示的非负整数 num，移除这个数中的 k 位数字，使得剩下的数字最小。

注意:
num 的长度小于 10002 且 ≥ k。
num 不会包含任何前导零。

示例 1 :
输入: num = "1432219", k = 3
输出: "1219"
解释: 移除掉三个数字 4, 3, 和 2 形成一个新的最小的数字 1219。

示例 2 :
输入: num = "10200", k = 1
输出: "200"
解释: 移掉首位的 1 剩下的数字为 200. 注意输出不能有任何前导零。

示例 3 :
输入: num = "10", k = 2
输出: "0"
解释: 从原数字移除所有的数字，剩余为空就是0。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-k-digits
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        '''
        堆栈解决
        :param num:
        :param k:
        :return:
        '''
        numStack=[]
        for d in num:
            while k and numStack and numStack[-1]>d:
                numStack.pop()
                k-=1
            numStack.append(d)
        finalStack=numStack[:-k] if k else numStack # 若序列位递增，则没有删除，直接删去末尾k个。

        return ''.join(finalStack).lstrip('0') or '0'


if __name__ == '__main__':
    S=Solution()
    print(S.removeKdigits('1432219',3))




