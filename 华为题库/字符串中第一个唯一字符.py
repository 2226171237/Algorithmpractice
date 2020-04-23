'''
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

案例:
s = "leetcode"
返回 0.

s = "loveleetcode",
返回 2.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/first-unique-character-in-a-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def firstUniqChar(self, s: str) -> int:
        '''

        :param s:
        :return:
        '''
        hashmap=dict()
        for ch in s:
            hashmap[ch]=hashmap.get(ch,0)+1
        for i in range(len(s)):
            if hashmap[s[i]]==1:
                return i
        return -1

if __name__ == '__main__':
    S=Solution()
    print(S.firstUniqChar('loveleetcode'))