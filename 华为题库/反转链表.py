'''
反转一个单链表。

示例:
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 原地反转
        pre=None
        cur=head
        while cur:
            t=cur.next
            cur.next=pre
            pre=cur
            cur=t
        return pre
    def visit(self,head:ListNode):
        node=head
        while node:
            print(node.val,end=' ')
            node=node.next
        print()
if __name__ == '__main__':
    S=Solution()
    head=ListNode(1)
    S.visit(head)
    head=S.reverseList(head)
    S.visit(head)


