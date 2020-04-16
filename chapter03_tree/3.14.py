# -*- coding=utf-8-*-
'''
如何实现方向DNS查找缓存。
即：二叉查找树Trie(字典树)
实现域名查找
如：74.125.200.106->google.com
'''


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, x):
        self.items.append(x)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return
        return self.items[-1]

    def size(self):
        return len(self.items)


class TrieNode:
    def __init__(self):
        CHARCOUT=11
        self.isLeaf=False
        self.url=None
        self.child=[None for _ in range(CHARCOUT)]

def getIndexFromChar(c):
    return 10 if c=='.' else ord(c)-ord('0')

def getCharFromIndex(index):
    return '.' if 10==index else str(index)


class DNSCache:
    def __init__(self):
        self.CHAR_COUNT=11
        self.root=TrieNode()

    def insert(self,ip,url):
        lens=len(ip)
        pCrawl=self.root
        level=0
        while level<lens:
            index=getIndexFromChar(ip[level])
            if pCrawl.child[index]==None:
                pCrawl.child[index]=TrieNode()
            pCrawl=pCrawl.child[index]
            level+=1

        pCrawl.isLeaf = True
        pCrawl.url = url


    def searchDNSCache(self,ip):
        pCrawl=self.root
        lens=len(ip)
        level=0
        while level<lens:
            index=getIndexFromChar(ip[level])
            if pCrawl.child[index]==None:
                return None
            pCrawl=pCrawl.child[index]
            level+=1
        if pCrawl!=None and pCrawl.isLeaf:
            return pCrawl.url
        return None

if __name__ == '__main__':
    ipAdds=['10.57.11.127','121.57.61.129','66.125.100.103']
    urls=['www.samsung.com','www.samsung.net','www.google.cn']
    cache=DNSCache()
    for i,ip in enumerate(ipAdds):
        cache.insert(ip,urls[i])

    ip='66.125.100.103'
    res_url=cache.searchDNSCache(ip)
    if res_url:
        print(ip,'->',res_url)
    else:
        print(ip,'-> none')