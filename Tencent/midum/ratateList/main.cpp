#include <iostream>

/**
 * 旋转链表
 * 给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。
示例 1:
输入: 1->2->3->4->5->NULL, k = 2
输出: 4->5->1->2->3->NULL
解释:
向右旋转 1 步: 5->1->2->3->4->NULL
向右旋转 2 步: 4->5->1->2->3->NULL
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rotate-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
 * @return
 */
 using namespace std;
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    int lengthOfList(ListNode *head)
    {
        int len=0;
        ListNode *pnode=head;
        while (pnode!=NULL)
        {
            len++;
            pnode=pnode->next;
        }
        return len;
    }
    ListNode* rotateRight(ListNode* head, int k)
    {
        if(NULL==head || NULL==head->next)
            return head;
        int listLen=lengthOfList(head);
        k=listLen-k%listLen;
        ListNode *subList=head;
        for(int i=1;i<k;i++)
        {
            subList=subList->next;
        }
        ListNode *tail=subList->next;
        if(tail==NULL) return head;
        ListNode *newhead=tail;
        subList->next=NULL;
        while(tail->next!=NULL)
        {
            tail=tail->next;
        }
        tail->next=head;
        return newhead;
    }
};

int main() {
    Solution S;
    ListNode *head;
    ListNode node1(1);
    ListNode node2(2);
    ListNode node3(3);
    ListNode node4(4);
    ListNode node5(5);
    head=&node1;
    node1.next=&node2;
    node2.next=&node3;
    node3.next=&node4;
    node4.next=&node5;
    ListNode *newhead=S.rotateRight(head,8);
    while (newhead!=NULL)
    {
        cout<<newhead->val<<' ';
        newhead=newhead->next;
    }
    return 0;
}
