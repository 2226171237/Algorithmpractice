
class Node:
    def __init__(self,key,x):
        self.val=x
        self.key=key
        self.prev=None
        self.next=None

class DoubleList:
    def __init__(self):
        self.head=Node(-1,-1)
        self.end=Node(-1,-1)
        self.head.next=self.end
        self.end.prev=self.head

    def is_empty(self):
        return self.head.next==self.end

    def appendNode(self,node):
        node.next=None
        node.prev=None
        self.end.prev.next=node
        node.prev=self.end.prev
        node.next=self.end
        self.end.prev=node

    def deleteNode(self,node):
        node.prev.next=node.next
        node.next.prev=node.prev

    def popleft(self):
        node=self.head.next
        self.deleteNode(node)
        return node

class LRUCache:
    def __init__(self,capacity):
        self.capacity=capacity
        self.cache=DoubleList()
        self.cacheMap=dict()
        self._size=0

    def get(self,key):
        if key not in self.cacheMap:
            return
        node=self.cacheMap[key]
        self.cache.deleteNode(node)
        self.cache.appendNode(node)
        return node.val

    def put(self,key,val):
        if key in self.cacheMap:
            node=self.cacheMap[key]
            node.val=val
            self.cache.deleteNode(node)
            self.cache.appendNode(node)
        else:
            node=Node(key,val)
            if self._size==self.capacity:
                del_node=self.cache.popleft()
                self.cacheMap.pop(del_node.key)
                self._size-=1
            self.cacheMap[key]=node
            self.cache.appendNode(node)
            self._size+=1


if __name__ == '__main__':
    cache=LRUCache(3)
    cache.put(1,2)
    cache.put(2,3)
    print(cache.get(1))
    cache.put(3,4)
    cache.put(4,5)
    cache.put(3,6)
    cache.put(6,7)
    cache.put(7,8)
