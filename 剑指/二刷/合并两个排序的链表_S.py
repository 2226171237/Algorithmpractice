'''
输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。

'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1==None:
            return l2
        if l2==None:
            return l1
        if l1.val<l2.val:
            l1.next=self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next=self.mergeTwoLists(l1,l2.next)
            return l2

if __name__ == '__main__':
    s=Solution()
    L1=ListNode(1)
    L1.next=ListNode(2)
    L1.next.next=ListNode(4)
    L2=ListNode(2)
    L2.next=ListNode(3)
    L2.next.next=ListNode(5)
    L=s.mergeTwoLists(L1,L2)
    print()
