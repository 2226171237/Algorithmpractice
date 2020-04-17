"""
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
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result=[]
        node1=l1
        node2=l2
        S,C=0,0  # 和与进位
        while node1 and node2:
            S=node1.val+node2.val+C
            if S>=10:
                S-=10
                C=1
            else:
                C=0
            result.append(S)
            node1=node1.next
            node2=node2.next
        # 解决剩余的高位
        node=node1 if node1 else node2
        while node:
            S=node.val+C
            if S>=10:
                S-=10
                C=1
            else:
                C=0
            result.append(S)
            node=node.next
        # 最后一个加和有进位
        if C==1:
            result.append(C)
        # 转成链表
        head=ListNode(result[0])
        node=head
        for x in result[1:]:
            node.next=ListNode(x)
            node=node.next
        return head

    def visit(self,result):
        node=result
        while node:
            print(node.val,end='->')
            node=node.next
        print()

    def buildList(self,L):
        head=ListNode(L[0])
        node=head
        for x in L[1:]:
            node.next=ListNode(x)
            node=node.next
        return head
if __name__ == '__main__':
    S=Solution()
    L1=S.buildList([1])
    L2=S.buildList([9,9])
    result=S.addTwoNumbers(L1,L2)
    S.visit(result)