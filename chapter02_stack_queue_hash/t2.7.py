#-*-coding=utf-8-*-
'''
如何设计一个排序系统。
请设计一个排序系统，能够让每个进入队伍的用户都能看到自己队列中所处的位置和变化，
队伍可能随时加入和退出；当有人退出影响到用户的位置排名时需及时反馈到用户。
'''
class User:
    def __init__(self,id,name):
        self.id=id
        self.name=name
        self.seq=1

    def getName(self):
        return self.name

    def setName(self,name):
        self.name=name

    def setSeq(self,seq):
        self.seq=seq

    def getSeq(self):
        return self.seq

    def getId(self):
        return self.id

    def equal(self,arg0):
        return self.getId()==arg0.getId()

    def __repr__(self):
        return 'id %s, name %s, seq %d' % (str(self.id),self.name,self.seq)

class LNode:
    def __init__(self,x,next=None):
        self.user=x
        self.next=next

class Queue:
    def __init__(self):
        self.Front=None
        self.Back=None
        self._length=0

    def is_empty(self):
        return self._length==0

    def enqueue(self,x):
        if self.is_empty():
            self.Front=self.Back=LNode(x)
        else:
            seq=self.getBack().getSeq()
            x.setSeq(seq+1)
            self.Back.next=LNode(x)
            self.Back=self.Back.next
        self._length+=1

    def dequeue(self):
        if self.is_empty():
            return None
        self.Front= self.Front.next
        node=self.Front
        while node:
            node.user.setSeq(node.user.getSeq()-1)
            node=node.next
        self._length-=1
        return node

    def getFront(self):
        if self.Front:
            return self.Front.user

    def getBack(self):
        if self.Back:
            return self.Back.user

    def size(self):
        return self._length

    def remove(self,x):
        if self.is_empty():
            return
        node=self.Front
        pred=self.Front
        isRemoved=False
        ishead=True
        while node:
            if node.user.getId()==x.getId() and not isRemoved :
                if ishead:
                    self.Front=node.next
                pred.next=node.next
                isRemoved=True
            pred=node
            node=node.next
            if isRemoved and node:
                node.user.setSeq(node.user.getSeq()-1)
            ishead=False

    def printList(self):
        if self.is_empty():
            return
        node =self.Front
        while node:
            print(node.user)
            node=node.next

if __name__ == '__main__':
    u1=User(1,'user1')
    u2=User(2,'user2')
    u3=User(3,'user3')
    u4=User(4,'user4')
    D=Queue()
    D.enqueue(u1)
    D.enqueue(u2)
    D.enqueue(u3)
    D.enqueue(u4)
    D.dequeue()
    D.remove(u3)
    D.enqueue(u1)
    D.enqueue(u3)
    D.remove(u2)
    D.printList()


