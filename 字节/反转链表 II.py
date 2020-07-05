'''
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

说明:
1 ≤ m ≤ n ≤ 链表长度。

示例:
输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-linked-list-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def reverseList(head):
    '''翻转链表'''
    if head==None or head.next==None:
        return head,head
    newhead=head
    node=head.next
    head.next=None
    end = head
    while node:
        nextnode=node.next
        node.next=newhead
        newhead=node
        node=nextnode
    return newhead,end

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        先断链，在翻转，后拼接
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if None==head:
            return None
        node=head
        prev=None
        for _ in range(m-1):
            prev=node
            node=node.next
        if prev:
            prev.next=None
        subhead=node
        for _ in range(m+1,n+1):
            node=node.next
        tailhead=node.next if node else None
        if node:
            node.next=None
        subhead,subend=reverseList(subhead)
        if prev:
            prev.next=subhead
        if subend:
            subend.next=tailhead
        return head if prev else subhead

if __name__ == '__main__':
    head=ListNode(1)
    head.next=ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    s=Solution()
    head=s.reverseBetween(head,1,1)
    print(head)