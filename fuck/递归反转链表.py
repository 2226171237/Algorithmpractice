
class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None

    def printList(self):
        print(self.val,end=' ')
        if self.next:
            self.next.printList()
        else:
            print()

head=ListNode(1)
head.next=ListNode(2)
head.next.next=ListNode(3)
head.next.next.next=ListNode(4)
head.next.next.next.next=ListNode(5)
head.printList()
# 反转整个链表
def reverseList(head:ListNode):
    if None==head or None==head.next:
        return head
    node=head.next
    newhead=reverseList(head.next)
    node.next=head
    head.next=None
    return newhead
head=reverseList(head)
head.printList()

# 反转链表前K个结点
tail=None
def reverseTopKList(head:ListNode,k):
    global tail
    if k==1:
        tail=head.next
        return head
    node=head.next
    newhead=reverseTopKList(head.next,k-1)
    node.next=head
    head.next=tail
    return newhead

head=reverseTopKList(head,3)
head.printList()

# 反转一部分 [m,n] 之间反转
def reverseListBetween(head:ListNode,m,n):
    if m==1:
        return reverseTopKList(head,n)
    head.next=reverseListBetween(head.next,m-1,n-1)
    return head

head=reverseListBetween(head,2,4)
head.printList()