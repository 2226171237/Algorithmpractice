'''
给定一个单词列表，我们将这个列表编码成一个索引字符串 S 与一个索引列表 A。
例如，如果这个列表是 ["time", "me", "bell"]，我们就可以将其表示为 S = "time#bell#" 和 indexes = [0, 2, 5]。
对于每一个索引，我们可以通过从字符串 S 中索引的位置开始读取字符串，直到 "#" 结束，来恢复我们之前的单词列表。
那么成功对给定单词列表进行编码的最小字符串长度是多少呢？

示例：
输入: words = ["time", "me", "bell"]
输出: 10
说明: S = "time#bell#" ， indexes = [0, 2, 5] 。

提示：
1 <= words.length <= 2000
1 <= words[i].length <= 7
每个单词都是小写字母 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/short-encoding-of-words
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class TrieNode:
    def __init__(self,layer):
        self.layer=layer
        self.childs=dict()

class Solution:
    def minimumLengthEncoding(self, words) -> int:
        '''
        查找，没有后缀的单词
        :param  list[str] words:
        :return:
        '''
        wordsets=set(words)
        for word in words:
            for i in range(1,len(word)+1):
                if word[i:] in wordsets:
                    wordsets.remove(word[i:])
        Lens=sum([len(word)+1 for word in wordsets])
        return Lens

    def minimumLengthEncoding2(self, words) -> int:
        '''
        字典树，Trie
        :param  list[str] words:
        :return:
        '''
        root=TrieNode(0) # 根节点
        # 构建Trie
        for word in words:
            node=root
            for w in word[::-1]:
                if w not in node.childs:
                    node.childs[w]=TrieNode(node.layer+1)
                node=node.childs[w]
        Lens=[0] # 全局变量
        def visit(root:TrieNode):  # DFS
            nonlocal Lens
            if len(root.childs)==0: # 叶节点
                Lens[0]+=root.layer+1
            else:
                for child in root.childs:
                    visit(root.childs[child])
        visit(root)
        return Lens[0]

    def minimumLengthEncoding3(self, words) -> int:
        '''
        反转字符串，排序
        :param words:
        :return:
        '''
        reversedWords=[word[::-1] for word in words]
        reversedWords=sorted(reversedWords)
        i=0
        Lens=0
        while i<len(reversedWords):
            if i+1<len(reversedWords) and reversedWords[i+1].startswith(reversedWords[i]):
                pass
            else:
                Lens+=len(reversedWords[i])+1
            i+=1
        return Lens

if __name__ == '__main__':
    S=Solution()
    print(S.minimumLengthEncoding(words = ["time", "me", "lime", "sometime", "hell", "shell"]))
    print(S.minimumLengthEncoding2(words=["time", "me", "lime", "sometime", "hell", "shell"]))
    print(S.minimumLengthEncoding3(words=["time", "me", "lime", "sometime", "hell", "shell"]))
