'''
请你为 最不经常使用（LFU）缓存算法设计并实现数据结构。它应该支持以下操作：get 和 put。

get(key) - 如果键存在于缓存中，则获取键的值（总是正数），否则返回 -1。
put(key, value) - 如果键已存在，则变更其值；如果键不存在，请插入键值对。
当缓存达到其容量时，则应该在插入新项之前，使最不经常使用的项无效。
在此问题中，当存在平局（即两个或更多个键具有相同使用频率）时，应该去除最久未使用的键。
「项的使用次数」就是自插入该项以来对其调用 get 和 put 函数的次数之和。使用次数会在对应项被移除后置为 0 。

进阶：
你是否可以在 O(1) 时间复杂度内执行两项操作？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lfu-cache
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Node:
    def __init__(self,key,val,frep=1,prev=None,next=None):
        self.key=key
        self.val=val
        self.prev=prev
        self.next=next
        self.frep=frep


class DoubleList:
    def __init__(self):
        self.head=Node(0,0)
        self.end=Node(0,0)
        self.head.next=self.end
        self.end.prev=self.head
        self._size=0

    def isEmpty(self):
        return self._size==0

    def addNode(self,node):
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
            node.next = self.end

        self._size+=1

    def delNode(self,node):
        node.prev.next=node.next
        node.next.prev=node.prev
        self._size-=1

    def top(self):
        return self.head.next

from collections import defaultdict
class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity=capacity
        self.cache=dict()
        self.frepMap=defaultdict(DoubleList)
        self.minFrep=1

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        node=self.cache[key]
        frep=node.frep
        frepList=self.frepMap[frep]
        frepList.delNode(node)
        node.frep+=1
        self.frepMap[frep+1].addNode(node)
        if self.minFrep==frep and frepList.isEmpty():
            self.minFrep+=1
        return node.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if self.capacity==0:
            return
        if key in self.cache:
            node=self.cache[key]
            frep=node.frep
            frepList=self.frepMap[frep]
            frepList.delNode(node)
            if self.minFrep==frep and frepList.isEmpty():
                self.minFrep+=1
            node.val=value
            node.frep+=1
            self.frepMap[frep+1].addNode(node)
        else:
            if len(self.cache)==self.capacity:
                node=self.frepMap[self.minFrep].top()
                self.frepMap[self.minFrep].delNode(node)
                self.cache.pop(node.key)

            node=Node(key,value)
            self.cache[key]=node
            self.minFrep=1
            self.frepMap[1].addNode(node)


if __name__ == '__main__':
    cache=LFUCache(3)
    cache.put(2,2)
    cache.put(1,1)
    print(cache.get(2))
    print(cache.get(1))
    print(cache.get(2))
    cache.put(3,3)
    cache.put(4, 4)
    print(cache.get(3))
    print(cache.get(2))
    print(cache.get(1))
    print(cache.get(4))