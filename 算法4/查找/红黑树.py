
RED=True
BLACK=False
class Node:
    def __init__(self,key,val,color,N,left=None,right=None):
        self.key=key
        self.val=val
        self.left=left
        self.right=right
        self.color=color
        self.N=N


def isRed(h:Node):
    if h == None:
        return False
    return h.color==RED

def size(x:Node):
    if x ==None:
        return 0
    else:
        return x.N

def rotateLeft(h:Node):
    x=h.right
    h.right=x.left
    x.left=h
    x.color=h.color
    h.color=RED
    x.N=h.N
    h.N=size(h.left)+size(h.right)+1
    return x

def rotateRight(h:Node):
    x=h.left
    h.left=x.right
    x.right=h
    x.color=h.color
    h.color=RED
    x.N=h.N
    h.N=size(h.left)+size(h.right)+1
    return x

def flipColor(h:Node):
    h.color=RED
    h.left.color=BLACK
    h.right.color=BLACK

def put(h:Node,key,val):
    if h==None:
        return Node(key,val,N=1,color=RED)
    if h.key>key:
        h.left=put(h.left,key,val)
    elif h.key<key:
        h.right=put(h.right,key,val)
    else:
        h.val=val
    if isRed(h.right) and not isRed(h.left):
        h=rotateLeft(h)
    if isRed(h.left) and isRed(h.left.left):
        h=rotateRight(h)
    if isRed(h.left) and isRed(h.right):
        flipColor(h)
    h.N=size(h.left)+h.right+1
    return h

class RBTS:
    def __init__(self):
        self.root=None

    def is_empty(self):
        return self.root==None

    def put(self,key,val):
        self.root=put(self.root,key,val)
        self.root.color=BLACK