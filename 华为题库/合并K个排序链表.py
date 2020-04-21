'''
合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:
输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-k-sorted-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists) -> ListNode:
        '''
        每次只合并两个链表,超时了。
        :param list[ListNode] lists:
        :return:
        '''
        ListNums=len(lists)
        if ListNums==1:
            return lists[0]

        def mergeList(head1:ListNode,head2:ListNode):
            if head1==None:
                return head2
            if head2==None:
                return head1
            if head1.val<head2.val:
                head1.next=mergeList(head1.next,head2)
                return head1
            else:
                head2.next=mergeList(head1,head2.next)
                return head2

        head=lists[0]
        for i in range(1,ListNums):
            head=mergeList(head,lists[i])
        return head

    def mergeKLists2(self, lists) -> ListNode:
        '''
        对上面进行分治，合并
        :param list[ListNode] lists:
        :return:
        '''
        ListNums=len(lists)
        if ListNums==1:
            return lists[0]

        def mergeList(head1:ListNode,head2:ListNode):
            if head1==None:
                return head2
            if head2==None:
                return head1
            if head1.val<head2.val:
                head1.next=mergeList(head1.next,head2)
                return head1
            else:
                head2.next=mergeList(head1,head2.next)
                return head2

        def sortLists(lists:list,begin,end):
            if begin>end:
                return None
            if begin==end:
                return lists[begin]
            mid=(begin+end)//2
            head1=sortLists(lists,begin,mid)
            head2=sortLists(lists,mid+1,end)
            return mergeList(head1,head2)

        return sortLists(lists,0,ListNums-1)

if __name__ == '__main__':
    S=Solution()


