

class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None

# 递归反转链表
def reversedList(head):
    if head==None or None==head.next:
        return head
    node=head.next
    new_head=reversedList(head.next)
    node.next=head
    head.next=None
    return new_head

head=ListNode(1)
head.next=ListNode(2)
head.next.next=ListNode(3)
head.next.next.next=ListNode(4)
new_head=reversedList(head)
while new_head:
    print(new_head.val,end=' ')
    new_head=new_head.next
print()

# 翻转前N个结点

successor1=None
def reversedListN(head,n):
    global successor1
    if n==1:
        successor1=head.next
        return head
    node=head.next
    new_head=reversedListN(head.next,n-1)
    node.next=head
    head.next=successor1
    return new_head


head=ListNode(1)
head.next=ListNode(2)
head.next.next=ListNode(3)
head.next.next.next=ListNode(4)
new_head=reversedListN(head,4)
while new_head:
    print(new_head.val,end=' ')
    new_head=new_head.next
print()


# 翻转一部分
def reversedPartList(head,m,n):
    if m==1:
        return reversedListN(head,n)
    new_head=reversedPartList(head.next,m-1,n-1)
    head.next=new_head
    return head

head=ListNode(1)
head.next=ListNode(2)
head.next.next=ListNode(3)
head.next.next.next=ListNode(4)
new_head=reversedPartList(head,2,3)
while new_head:
    print(new_head.val,end=' ')
    new_head=new_head.next
print()


