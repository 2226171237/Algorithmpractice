'''
运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制。它应该支持以下操作： 获取数据 get 和 写入数据 put 。

获取数据 get(key) - 如果关键字 (key) 存在于缓存中，则获取关键字的值（总是正数），否则返回 -1。
写入数据 put(key, value) - 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字/值」。
当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lru-cache
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Node:
    def __init__(self,key,val,prev=None,next=None):
        self.key=key
        self.val=val
        self.prev=prev
        self.next=next


class DoubleQueue:
    def __init__(self):
        self.head=Node(0,0)
        self.end=Node(0,0)
        self._size=0
        self.head.next=self.end
        self.end.prev=self.head

    def isEmpty(self):
        return self._size==0

    def put(self,node):
        node.prev=None
        node.next=None
        if self.isEmpty():
            self.head.next=node
            node.prev=self.head
            node.next=self.end
            self.end.prev=node
        else:
            self.end.prev.next=node
            node.prev=self.end.prev
            self.end.prev=node
            node.next=self.end
        self._size+=1

    def delete(self,node):
        node.prev.next=node.next
        node.next.prev=node.prev
        self._size-=1

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity=capacity
        self.cache=dict()
        self.lfuDeque=DoubleQueue()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        node=self.cache[key]
        self.lfuDeque.delete(node)
        self.lfuDeque.put(node)
        return node.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            node=self.cache[key]
            node.val=value
            self.lfuDeque.delete(node)
            self.lfuDeque.put(node)
        else:
            if len(self.cache)==self.capacity:
                node=self.lfuDeque.head.next
                self.lfuDeque.delete(node)
                self.cache.pop(node.key)
            node=Node(key,value)
            self.cache[key]=node
            self.lfuDeque.put(node)

if __name__ == '__main__':
    cache=LRUCache(2)
    cache.put(1,1)
    cache.put(2,2)
    print(cache.get(1))
    cache.put(3,3)
    print(cache.get(2))
    cache.put(4, 4)
    print(cache.get(1))
    print(cache.get(3))
    print(cache.get(4))