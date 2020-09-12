
# 问题1：最长回文子串
def palindrome(s,low,high):
    while low>=0 and high<len(s):
        if s[low]==s[high]:
            low-=1
            high+=1
        else:
            break
    low+=1
    high-=1
    return s[low:high+1]

def longestHuiwenSubStr(s):
    if len(s)==0:
        return ''
    res=s[0]
    for i in range(len(s)-1):
        subS=palindrome(s,i,i)
        if len(res)<len(subS):
            res=subS
        subS=palindrome(s,i,i+1)
        if len(res)<len(subS):
            res=subS
    return res

print(longestHuiwenSubStr('hhwhwhh'))

# 问题2：如何判断一个「单链表」是不是回文。
class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None

def isHuiwenList(head):
    left=head
    def isValid(right):
        nonlocal left
        if None==right:
            return True
        res=isValid(right.next)
        res=res and left.val==right.val
        left=left.next
        return res
    return isValid(head.next)

head=ListNode(1)
head.next=ListNode(2)
head.next.next=ListNode(3)
head.next.next.next=ListNode(3)
head.next.next.next.next=ListNode(1)
print(isHuiwenList(head))

