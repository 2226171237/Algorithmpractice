'''
在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。

示例 1:
输入: 4->2->1->3
输出: 1->2->3->4
示例 2:
输入: -1->5->3->4->0
输出: -1->0->3->4->5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sort-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head):
        if head==None or head.next==None:
            return head
        slow=head
        fast=head
        prev=None
        while fast and fast.next:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        prev.next=None
        left=self.sortList(head)
        right=self.sortList(slow)
        return self.merge(left,right)

    def merge(self,head1,head2):
        if head1==None:
            return head2
        if head2==None:
            return head1
        if head1.val<head2.val:
            head1.next=self.merge(head1.next,head2)
            return head1
        else:
            head2.next=self.merge(head1,head2.next)
            return head2


if __name__ == '__main__':
    head=ListNode(4)
    head.next=ListNode(2)
    head.next.next=ListNode(1)
    head.next.next.next=ListNode(3)
    s=Solution()
    new_head=s.sortList(head)
    while new_head:
        print(new_head.val,end=' ')
        new_head=new_head.next
