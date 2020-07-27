'''
输入两个链表，找出它们的第一个公共节点。
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if None==headA or None==headB:
            return None
        node=headA
        while node.next:
            node=node.next
        node.next=headB

        slow=headA
        fast=headA
        while slow!=fast:
            slow=slow.next
            fast=fast.next
            if fast==None or fast.next==None:
                return None
            else:
                fast=fast.next
        slow=headA
        while slow!=fast:
            slow=slow.next
            fast=fast.next
        return slow

    def getIntersectionNode2(self, headA, headB):
        if None==headA or None==headB:
            return None
        node1=headA
        node2=headB
        while node1!=node2:
            node1=headB if node1==None else node1.next
            node2=headA if node2==None else node2.next
        return node1

