'''
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：
给定一个链表: 1->2->3->4->5, 和 n = 2.
当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：
给定的 n 保证是有效的。

进阶：
你能尝试使用一趟扫描实现吗？
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head==None:
            return None
        slow=head
        fast=head
        for _ in range(n):
            fast=fast.next
        prev=None
        while fast:
            fast=fast.next
            prev=slow
            slow=slow.next
        if prev==None:
            return head.next
        else:
            prev.next=slow.next
            slow.next=None
        return head


if __name__ == '__main__':
    s=Solution()
    L=ListNode(1)
    L.next=ListNode(2)
    L.next.next=ListNode(3)
    L=s.removeNthFromEnd(L,2)
    node=L
    while node:
        print(node.val,end=' ')
        node=node.next