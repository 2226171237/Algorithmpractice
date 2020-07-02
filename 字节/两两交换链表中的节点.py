'''
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例:
给定 1->2->3->4, 你应该返回 2->1->4->3.
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/swap-nodes-in-pairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if None==head:
            return None
        if None==head.next:
            return head

        prev=None
        node1=head
        node2=head.next
        while node1 and node2:
            node1.next=node2.next
            node2.next=node1
            if prev==None:
                head=node2
            else:
                prev.next=node2
            prev=node1
            node1=node1.next
            if None==node1:
                break
            node2=node1.next

        return head

    def swapPairs2(self, head):
        '''递归版'''
        if None==head or None==head.next:
            return head
        node=head.next
        head.next=self.swapPairs(node.next)
        node.next=head
        return node


if __name__ == '__main__':
    s=Solution()
    head=ListNode(1)
    head.next=ListNode(2)
    head.next.next = ListNode(3)

    head=s.swapPairs2(head)
    while head:
        print(head.val,end=' ')
        head=head.next


