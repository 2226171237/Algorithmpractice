

class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None


Left=None
def isPalindrome(head:ListNode):
    global Left
    Left=head
    return travel(head.next)

def travel(right):
    global Left
    if right==None:
        return True
    res=travel(right.next)
    res=res and right.val==Left.val
    Left=Left.next
    return res
