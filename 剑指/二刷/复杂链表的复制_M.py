'''
请实现 copyRandomList 函数，复制一个复杂链表。在复杂链表中，每个节点除了有一个 next 指针指向下一个节点，
还有一个 random 指针指向链表中的任意节点或者 null。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/fu-za-lian-biao-de-fu-zhi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if None==head:
            return None
        node=head
        while node:
            node.next=Node(node.val,node.next)
            node=node.next.next

        node=head
        while node:
            node.next.random=node.random.next if node.random else None
            node=node.next.next

        node1=head
        newHead=head.next
        node2=head.next
        while node1:
            node1.next=node2.next
            node1=node1.next
            if None==node1:
                break
            node2.next=node1.next
            node2=node2.next

        return newHead


if __name__ == '__main__':
    s=Solution()
    head=Node(1)
    head.next=Node(2)
    head.next.next=Node(3)
    head.random=head.next.next
    head.next.next.random=head
    s.copyRandomList(head)