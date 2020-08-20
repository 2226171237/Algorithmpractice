'''
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

示例:
输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
说明：
所有输入均为小写字母。
不考虑答案输出的顺序。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/group-anagrams
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Node:
    def __init__(self,id,x):
        self.string=''.join(sorted(x))
        self.id=id
    def __lt__(self, other):
        return self.string<other.string

def getCountsStr(word):
    tmp=[0 for _ in range(26)]
    for w in word:
        tmp[ord(w)-ord('a')]+=1
    return ''.join(map(str,tmp))

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        tmp=[Node(i,strs[i]) for i in range(len(strs))]
        tmp.sort()
        result=dict()
        for p in tmp:
            if p.string not in result:
                result[p.string]=[strs[p.id]]
            else:
                result[p.string].append(strs[p.id])
        return list(result.values())

    def groupAnagrams2(self, strs):
        '''计数法'''
        d=dict()
        for w in strs:
            word=getCountsStr(w)
            if word not in d:
                d[word]=[w]
            else:
                d[word].append(w)
        return list(d.values())

if __name__ == '__main__':
    s=Solution()
    print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(s.groupAnagrams2(["eat", "tea", "tan", "ate", "nat", "bat"]))