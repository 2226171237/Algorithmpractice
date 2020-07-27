


class Node:
    def __init__(self,x):
        self.val=x
        self.prev=None
        self.next=None

class DoubleList:
    def __init__(self):
        self.head=Node(-1)
        self.end=Node(-1)
        self.head.next=self.end
        self.end.prev=self.head
        self._size=0

    def is_empty(self):
        return self._size==0

    def append(self,node):
        node.next=None
        node.prev=None
        self.end.prev.next=node
        node.prev=self.end.prev
        node.next=self.end
        self.end.prev=node
        self._size+=1

    def popleft(self):
        if self.is_empty():
            return None
        node=self.head.next
        self.head.next=node.next
        node.next.prev=self.head
        return node

    def delete(self,node):
        node.prev.next=node.next
        node.next.prev=node.prev

    def peakleft(self):
        if self.is_empty():
            return None
        return self.head.next

class LRUCache:
    def __init__(self,capacity=16):
        self.capacity=capacity
        self.cache=DoubleList()
        self.cache_map=dict()
        self._size=0

    def size(self):
        return self._size

    def put(self,key,val):
        if key in self.cache_map:
            node=self.cache_map[key]
            node.val=val
            self.cache.delete(node)
            self.cache.append(node)
        else:
            node=Node(val)
            if self.size()==self.capacity:
                del_node=self.cache.popleft()
                self.cache_map.pop(del_node.val)
                self._size -= 1
            self.cache_map[key]=node
            self.cache.append(node)
            self._size+=1

    def get(self,key):
        if key not in self.cache_map:
            return -1
        node=self.cache_map[key]
        self.cache.delete(node)
        self.cache.append(node)
        return node.val




