
class Node:
    def __init__(self,val,R):
        self.val=val
        self.next=[None for _ in range(R)]

class TrieST:
    '''单词查找树'''
    def __init__(self,R=256):
        self.R=R
        self._size=0
        self.root=Node(None,self.R)
    def isEmpty(self):
        return self._size==0

    def size(self):
        return self._size

    def put(self,key:str,val):
        node=self.root
        for ch in key:
            if None==node.next[ord(ch)]:
                node.next[ord(ch)]=Node(None,self.R)
            node=node.next[ord(ch)]
        node.val=val
        self._size+=1 if val else -1

    def get(self,key:str):
        node=self.root
        for ch in key:
            node=node.next[ord(ch)]
            if node==None:
                return None
        return node.val

    def keyWithPrefix(self,pre):
        '''前缀字符串'''
        node=self.root
        for ch in pre:
            node=node.next[ord(ch)]
            if node==None:
                return  []
        result=[]
        self.collect(node,pre,result)
        return result

    def collect(self,node:Node,s:str,result:list):
        '''获取所有字符串'''
        if None==node:
            return
        if node.val!=None:
            result.append(s)
        for i,nextnode in enumerate(node.next):
            self.collect(nextnode,s+chr(i),result)

    def delete(self,key):

        def _delete(node,key,d):
            if node==None:
                return
            if d==len(key):
                node.val=None
            else:
                c=ord(key[d])
                node.next[c]=_delete(node[c],key,d+1)
            if node.val!=None:
                return node
            for i,xnode in enumerate(node.next):
                if xnode!=None:
                    return xnode
            return None

        self.root=_delete(self.root,key,0)

class TNode:
    def __init__(self,val,char,left=None,mid=None,right=None):
        self.val=val
        self.char=char
        self.left=left
        self.mid=mid
        self.right=right


def put(root,key,val,d):
    c=key[d]
    if None==root:
        root=TNode(None,c)
    if c<root.char:
        root.left=put(root.left,key,val,d)
    elif c>root.char:
        root.right=put(root.right,key,val,d)
    elif d<len(key)-1:
        root.mid=put(root.mid,key,val,d+1)
    else:
        root.val=val
    return root

def get(root,key,d):
    if None==root:
        return None
    c=key[d]
    if c<root.char:
        return get(root.left,key,d)
    elif c>root.char:
        return get(root.right,key,d)
    elif d<len(key)-1:
        return get(root.mid,key,d+1)
    else:
        return root

class TST:
    '''三向查找树'''
    def __init__(self):
        self.root=None

    def isEmpty(self):
        return None==self.root
    
    def put(self,key,val):
        self.root=put(self.root,key,val,0)

    def get(self,key):
        x=get(self.root,key,0)
        return x.val if x else x

if __name__ == '__main__':
    trie=TrieST()
    key_vals=[('she',0),('sells',1),('sea',2),('shells',3),('by',4),('the',5),('sea',6),('shore',7)]
    for key,val in key_vals:
        trie.put(key,val)

    for key,_ in key_vals:
        print(key,'=',trie.get(key))

    print(trie.keyWithPrefix('she'))
