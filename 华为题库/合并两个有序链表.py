'''
将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-two-sorted-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''
        遍历
        :param l1:
        :param l2:
        :return:
        '''
        if None==l1:
            return l2
        if None==l2:
            return l1
        node1=l1
        node2=l2
        if node1.val<=node2.val:
            head=node1
            node1=node1.next
        else:
            head=node2
            node2=node2.next

        node=head
        while node1 and node2:
            if node1.val<=node2.val:
                node.next=node1
                node1=node1.next
            else:
                node.next=node2
                node2=node2.next
            node=node.next
        restnode=node1 if node1 else node2
        node.next=restnode
        return head

    def mergeTwoLists2(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''
        递归
        :param l1:
        :param l2:
        :return:
        '''
        if None == l1:
            return l2
        if None == l2:
            return l1
        if l1.val<l2.val:
            l1.next=self.mergeTwoLists2(l1.next,l2)
            return l1
        else:
            l2.next=self.mergeTwoLists2(l1,l2.next)
            return l2

if __name__ == '__main__':
    S=Solution()
    node1=ListNode(1)
    node1.next=ListNode(2)
    node1.next.next=ListNode(4)
    node2=ListNode(1)
    node2.next=ListNode(3)
    head=S.mergeTwoLists(node1,node2)
    while head:
        print(head.val,end='->')
        head=head.next