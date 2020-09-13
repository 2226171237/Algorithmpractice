


# 敏感字替换成 ‘*’

def find(txt,target):
    '''单词查找 BM 算法'''
    right=dict()
    for i,x in enumerate(target):
        right[x]=i
    i=0
    txt_len=len(txt)
    target_len=len(target)
    step=1
    while i<=txt_len-target_len:
        j=target_len-1
        while j>=0:
            if txt[i+j]!=target[j]:
                step=j-(right[txt[i+j]] if txt[i+j] in right else -1)
                break
            j-=1
        if j==-1:
            return i
        step=max(1,step)
        i+=step
    return -1

print(find('helloworld','llow'))


# 单词查找树
class Node:
    def __init__(self,end=False):
        self.end=end
        self.child=dict()

class Trie:
    def __init__(self):
        self.root=Node()
        self.words=0

    def __len__(self):
        return self.words

    def addWrod(self,word):
        node=self.root
        for x in word:
            if x not in node.child:
                node.child[x]=Node()
            node=node.child[x]
        node.end=True
        self.words+=1

    def search(self,word):
        node=self.root
        for x in word:
            if x not in node.child:
                return False
            node=node.child[x]
        return node.end


def findWord(txt,words):
    trie=Trie()
    for word in words:
        trie.addWrod(word)
    p1=0
    p2=0
    node=trie.root
    result=[]
    while p1<len(txt):
        x=txt[p1]
        if x in node.child:
            node=node.child[x]
            if node.end:
                #txt[p2:p1+1]='*'
                result.append('*')
                p1=p1+1
                p2=p1
                node=trie.root
            else:
                p1+=1
        else:
            result.append(txt[p2])
            node = trie.root
            p1=p2+1
            p2=p1
    return ''.join(result)

print(findWord('are you ok? how old love you great bad fuck gass',['fuck','gass','tick','love']))

