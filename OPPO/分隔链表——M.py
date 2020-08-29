'''
给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。
你应当保留两个分区中每个节点的初始相对位置。

示例:
输入: head = 1->4->3->2->5->2, x = 3
输出: 1->2->2->4->3->5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/partition-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        left=[]
        node=head
        prev=None
        righthead=None
        while node:
            if node.val<x:
                left.append(node)
                if prev:
                    prev.next=node.next
            else:
                prev=node
                if righthead==None:
                    righthead=node
            node=node.next
        if len(left)==0:
            return righthead
        newhead=left[0]
        node=newhead
        for i in range(1,len(left)):
            node.next=left[i]
            node=left[i]
        node.next=righthead
        return newhead

if __name__ == '__main__':
    head=ListNode(1)
    head.next=ListNode(4)
    head.next.next=ListNode(3)
    head.next.next.next=ListNode(2)
    head.next.next.next.next=ListNode(5)
    head.next.next.next.next.next=ListNode(2)
    s=Solution()
    head=s.partition(head,4)
    while head:
        print(head.val,end=' ')
        head=head.next


