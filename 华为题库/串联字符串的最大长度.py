'''
给定一个字符串数组 arr，字符串 s 是将 arr 某一子序列字符串连接所得的字符串，
如果 s 中的每一个字符都只出现过一次，那么它就是一个可行解。
请返回所有可行解 s 中最长长度。

示例 1：
输入：arr = ["un","iq","ue"]
输出：4
解释：所有可能的串联组合是 "","un","iq","ue","uniq" 和 "ique"，最大长度为 4。

示例 2：
输入：arr = ["cha","r","act","ers"]
输出：6
解释：可能的解答有 "chaers" 和 "acters"。

示例 3：
输入：arr = ["abcdefghijklmnopqrstuvwxyz"]
输出：26
 
提示：
1 <= arr.length <= 16
1 <= arr[i].length <= 26
arr[i] 中只含有小写英文字母

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

def isDup(s):
    n=0
    for ch in s:
        t=1<<(ord(ch)-ord('a'))
        if n&t!=0:
            return True
        else:
            n|=t
    return False

def isDup2Str(s1,s2):
    for ch in s2:
        if ch in s1:
            return True
    return False

class Solution:
    def maxLength(self, arr):
        '''
        枚举,选与不选
        :param list[str] arr:
        :return: int
        '''
        maxLen=[0]
        def getmaxLen(arr,i,s,strlen):
            if i==len(arr):
                return
            if isDup(arr[i]) or isDup2Str(s,arr[i]): # 不满足条件，直接不选
                getmaxLen(arr,i+1,s,strlen)
            else: # 满足条件，则也选，也不选
                maxLen[0]=max(maxLen[0],strlen+len(arr[i]))
                getmaxLen(arr,i+1,s+arr[i],strlen+len(arr[i])) # 选
                getmaxLen(arr,i+1,s,strlen)                    # 不选
        getmaxLen(arr,0,'',0)
        return maxLen[0]


if __name__ == '__main__':
    S=Solution()
    print(S.maxLength(["a", "abc", "d", "de", "def"]))
