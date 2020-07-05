'''
给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。
它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。
你可以假设除了数字 0 之外，这两个数字都不会以零开头。

进阶：
如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。

示例：
输入：(7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 8 -> 0 -> 7
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def reverseList(head):
    if head==None or None==head.next:
        return head
    node=head.next
    newhead=reverseList(head.next)
    node.next=head
    head.next=None
    return newhead

def add(head,c):
    if None==head:
        if c==0:
            return None
        else:
            return ListNode(c)
    s,c=(head.val+c)%10,(head.val+c)//10
    node=ListNode(s)
    node.next=add(head.next,c)
    return node

def twoAdd(head1,head2,c):
    if head1==None:
        return add(head2,c)
    if head2==None:
        return add(head1,c)
    s=head1.val+head2.val+c
    s,c=s%10,s//10
    node=ListNode(s)
    node.next=twoAdd(head1.next,head2.next,c)
    return node

def addStack(s1,c,head):
    if len(s1)==0:
        if c==0:
            return head
        else:
            node=ListNode(c)
            node.next=head
            return node
    s=s1.pop()+c
    s,c=s%10,s//10
    node=ListNode(s)
    node.next=head
    head=node
    head=addStack(s1,c,head)
    return head

def addTwoStack(s1,s2,c,head):
    if len(s1)==0:
        return addStack(s2,c,head)
    if len(s2)==0:
        return addStack(s1,c,head)
    s=s1.pop()+s2.pop()+c
    s,c=s%10,s//10
    node=ListNode(s)
    node.next=head
    head=node
    head=addTwoStack(s1,s2,c,head)
    return head

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head1=reverseList(l1)
        head2=reverseList(l2)
        head=twoAdd(head1,head2,0)
        return reverseList(head)

    def addTwoNumbers2(self, l1, l2):
        s1=[]
        s2=[]
        node=l1
        while node:
            s1.append(node.val)
            node=node.next
        node=l2
        while node:
            s2.append(node.val)
            node=node.next

        return addTwoStack(s1,s2,0,None)

head=addTwoStack([1,2,3],[3,4],0,None)