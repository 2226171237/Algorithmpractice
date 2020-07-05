'''
给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
示例 1:
给定链表 1->2->3->4, 重新排列为 1->4->2->3.
示例 2:
给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reorder-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head):
    if None==head or None==head.next:
        return head
    node=head.next
    newhead=reverseList(head.next)
    node.next=head
    head.next=None
    return newhead

def merge(head1,head2):
    if None==head1:
        return head2
    if None==head2:
        return head1
    node1=head1.next
    head1.next=head2
    node2=head2.next
    head2.next=merge(node1,node2)
    return head1

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if None==head or head.next==None:
            return head

        # 找中点
        slow=head
        fast=head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        # 分割链表
        taihead=slow.next
        slow.next=None
        # 进行翻转
        taihead=reverseList(taihead)
        # 合并
        head=merge(head,taihead)
        return head

if __name__ == '__main__':
    s=Solution()
    head=ListNode(1)
    head.next=ListNode(2)
    head.next.next=ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head=s.reorderList(head)
    print(head)

