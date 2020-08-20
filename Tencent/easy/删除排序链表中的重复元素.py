'''
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

示例 1:
输入: 1->1->2
输出: 1->2
示例 2:
输入: 1->1->2->3->3
输出: 1->2->3
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if None==head or None==head.next:
            return head
        prevnode=head
        nextnode=prevnode.next
        while nextnode:
            while nextnode and prevnode.val==nextnode.val:
                nextnode= nextnode.next
            prevnode.next=nextnode
            prevnode=nextnode
        return head

if __name__ == '__main__':
    head=ListNode(1)
    head.next=ListNode(1)
    head.next.next=ListNode(2)
    head.next.next.next=ListNode(3)
    head.next.next.next.next=ListNode(3)
    S=Solution()
    head=S.deleteDuplicates(head)
    while head:
        print(head.val,end=' ')
        head=head.next
