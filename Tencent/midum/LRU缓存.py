'''
设计和构建一个“最近最少使用”缓存，该缓存会删除最近最少使用的项目。缓存应该从键映射到值(允许你插入和检索特定键对应的值)，
并在初始化时指定最大容量。当缓存被填满时，它应该删除最近最少使用的项目。
它应该支持以下操作： 获取数据 get 和 写入数据 put 。

获取数据 get(key) - 如果密钥 (key) 存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。
写入数据 put(key, value) - 如果密钥不存在，则写入其数据值。当缓存容量达到上限时，
它应该在写入新数据之前删除最近最少使用的数据值，从而为新的数据值留出空间。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lru-cache-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Node:
    def __init__(self,x,key):
        self.val=x
        self.key=key
        self.pre=None
        self.next=None

class DoubleList:
    def __init__(self):
        self.head=Node(-1,-1)
        self.end=Node(-1,-1)
        self.head.next=self.end
        self.end.pre=self.head
        self._size=0

    def isEmpty(self):
        return self._size==0

    def append(self,node):
        node.next=None
        node.pre=None
        self.end.pre.next=node
        node.pre=self.end.pre
        self.end.pre=node
        node.next=self.end
        self._size+=1

    def delete(self,node):
        node.pre.next=node.next
        node.next.pre=node.pre
        self._size-=1

    def popleft(self):
        if self.isEmpty():
            return
        node=self.head.next
        self.head.next=self.head.next.next
        self.head.next.pre=self.head
        self._size-=1
        return node.key

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity=capacity
        self.size=0
        self.cache=dict()
        self.cachelist=DoubleList()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        node=self.cache[key]
        self.cachelist.delete(node)
        self.cachelist.append(node)
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
            self.cachelist.delete(node)
            self.cachelist.append(node)
        else:
            node=Node(value,key)
            self.cache[key]=node
            if self.size==self.capacity:
                oldkey=self.cachelist.popleft()
                self.cache.pop(oldkey)
                self.size-=1
            self.cachelist.append(node)
            self.size+=1

