'''
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        def add(head,c):
            if head==None:
                if c==0:
                    return None
                else:
                    return ListNode(c)
            s=head.val+c
            s,c=s%10,s//10
            node=ListNode(s)
            node.next=add(head.next,c)
            return node

        def addTwo(l1,l2,c):
            if l1==None:
                return add(l2,c)
            if l2==None:
                return add(l1,c)
            s=l1.val+l2.val+c
            s,c=s%10,s//10
            node=ListNode(s)
            node.next=addTwo(l1.next,l2.next,c)
            return node

        return addTwo(l1,l2,0)


if __name__ == '__main__':
    s=Solution()
    l1=ListNode(2)
    l1.next=ListNode(4)
    l1.next.next=ListNode(3)
    l2=ListNode(5)
    node=s.addTwoNumbers(l1,l2)

    while node:
        print(node.val,end=' ')
        node=node.next
