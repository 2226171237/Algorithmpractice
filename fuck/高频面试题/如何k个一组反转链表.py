

class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None


def reversePart(nodea,nodeb):
    prev=None
    cur=nodea
    child= nodea.next
    while cur!=nodeb:
        child=nodea.next
        cur.next=prev
        prev=cur
        cur=child
    return prev

def reverse(head,k):
    if None==head:
        return None
    a=head
    b=head
    for i in range(k):
        if b==None:return head
        b=b.next
    newhead=reversePart(a,b)
    a.next=reverse(b,k)
    return newhead
