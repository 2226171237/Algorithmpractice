'''
定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。
0 <= 节点个数 <= 5000
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None:
            return head
        prev=None
        current=head
        next=current.next
        while next:
            tmp=next.next
            current.next=prev
            next.next=current
            prev=current
            current=next
            next=tmp
        current.next=prev
        return current

    def reverseList2(self, head):
        if head==None:
            return head
        new_head=head
        node=head.next
        new_head.next=None
        while node:
            tmp=node.next
            node.next=new_head
            new_head=node
            node=tmp
        return new_head

if __name__ == '__main__':
    head=None
    node = head
    while node:
        print(node.val)
        node = node.next

    S=Solution()
    head=S.reverseList(head)
    node=head
    while node:
        print(node.val)
        node=node.next
