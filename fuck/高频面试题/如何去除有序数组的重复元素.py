

def removeDupArray(arr):
    slow=0
    fast=1
    while fast<len(arr):
        if arr[fast]!=arr[slow]: # 新元素
            slow+=1
            arr[slow]=arr[fast]
        fast+=1   # 重复元素
    return arr[:slow+1]

print(removeDupArray([1,1,1,2,2,2,3,3,4,5,6,6,7,7]))

class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None

def removeDupList(head):
    if head==None or None==head.next:
        return head
    slow=head
    fast=head.next
    while fast:
        if slow.val!=fast.val:
            slow=slow.next
            slow.val=fast.val
        else:
            fast=fast.next
    slow.next=None
    return head

head=ListNode(1)
head.next=ListNode(2)
head.next.next=ListNode(3)
head.next.next.next=ListNode(3)
head=removeDupList(head)
while head:
    print(head.val,end=' ')
    head=head.next
print()
