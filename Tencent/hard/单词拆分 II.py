'''
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，在字符串中增加空格来构建一个句子，
使得句子中所有的单词都在词典中。返回所有这些可能的句子。

说明：
分隔时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。
示例 1：
输入:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
输出:
[
  "cats and dog",
  "cat sand dog"
]
示例 2：
输入:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
输出:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
解释: 注意你可以重复使用字典中的单词。
示例 3：
输入:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
输出:
[]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-break-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        记忆化+回溯
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        d=set()
        for word in wordDict:
            d.add(word)
        result=[]
        mem=dict()
        def dfs(s,path):
            if s in mem:
                for t in mem[s]:
                    if t.endswith('ok') and len(t)>2:
                        result.append(' '.join(path)+' '+t[:-3])
                return mem[s]
            if 0==len(s):
                result.append(' '.join(path))
                return ["ok"]
            res=[]
            for i in range(len(s)):
                word=s[:i+1]
                if word in d:
                    path.append(word)
                    tmp=dfs(s[i+1:],path)
                    for t in tmp:
                        if t.endswith('ok'):
                            res.append(word+' '+t)
                    path.pop()
            mem[s]=res[:]
            return res
        dfs(s,[])
        return result

if __name__ == '__main__':
    s=Solution()
    print(s.wordBreak("catsanddog",["cat","cats","and","sand","dog"]))
