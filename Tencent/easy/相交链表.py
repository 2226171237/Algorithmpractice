'''
编写一个程序，找到两个单链表相交的起始节点。
'''

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
        node1=headA
        node2=headB
        if node1==None or node2==None:
            return None
        while node1!=node2:
            if node1.next==None and node2.next==None:
                return None
            node1=node1.next if node1.next else headB
            node2=node2.next if node2.next else headA
        return node1

if __name__ == '__main__':

    s=Solution()
