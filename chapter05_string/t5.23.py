'''
如何查找到达目标词的最短链长度？
给定一个词典和两个长度相同的开始和目标单词。找到从开始到目标最小链的长度。如果它存在，那么这条链
中相邻单词只有一个字符不同，而链中每个单词都是有效的单词，即它存在于词典中。可以假设词典中存在
目标字，所有词典词的长度相同。
'''

from collections import deque
def isAdjacent(a,b):
    diff=0
    i=0
    while i<len(a):
        if a[i]!=b[i]:
            diff+=1
        if diff>1:
            return False
        i+=1
    return diff==1

class Item:
    def __init__(self,str,lens):
        self.str=str
        self.lens=lens

def getShortestPathLens(D,start,target):
    q=deque()
    item=Item(start,1)
    q.append(item)
    while len(q)>0:
        temp=q[0]
        q.pop()
        for t in D:

            if isAdjacent(temp.str,t):
                item.str=t
                item.lens=temp.lens+1
                q.append(item)
                D.remove(t)
                if t == target:
                    return item.lens
    return 0

if __name__ == '__main__':
    D=['pooN','pbcc','zamc','poIc','pbca','pbIc','poIN']
    print(getShortestPathLens(D,'TooN','pbca'))