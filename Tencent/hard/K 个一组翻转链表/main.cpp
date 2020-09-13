#include <iostream>

using namespace std;
/**
 * 给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
 * k 是一个正整数，它的值小于或等于链表的长度。
 * 如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

 * 示例：
 * 给你这个链表：1->2->3->4->5
 * 当 k = 2 时，应当返回: 2->1->4->3->5
 * 当 k = 3 时，应当返回: 3->2->1->4->5
*/


struct ListNode {
     int val;
     ListNode *next;
     ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
private:
    ListNode *tmp;
public:
    // 全部翻转链表
    ListNode* reverseAll(ListNode* head)
    {
        if(head==NULL || head->next==NULL)
            return head;
        ListNode *node=head->next;
        ListNode *newhead=reverseAll(head->next);
        node->next=head;
        return newhead;
    }
    // 翻转链表前个结点
    ListNode* reverseKFirst(ListNode*head,int k)
    {
        if (head==NULL || head->next==NULL)
            return head;
        if(k==1){
            tmp=head->next;
            return head;
        }
        ListNode *node=head->next;
        ListNode *newhead=reverseKFirst(head->next,k-1);
        head->next=tmp;
        return newhead;
    }

    ListNode* reversePart(ListNode *a,ListNode* b)
    {
        ListNode *prev=NULL;
        ListNode *cur=a;
        ListNode *child=a;
        while(cur!=b)
        {
            child=cur->next;
            cur->next=prev;
            prev=cur;
            cur=child;
        }
        return prev;
    }
    // 每 k 个一组翻转链表
    ListNode* reverseKGroup(ListNode* head, int k) {
        if(head==NULL || head->next==NULL)
            return head;
        ListNode *a=head;
        ListNode *b=head;
        for(int i=0;i<k;i++)
        {
            if(b==NULL) return head;
            b=b->next;
        }
        ListNode *newhead=reversePart(a,b);
        a->next=reverseKGroup(b,k);
        return newhead;
    }
};

int main()
{
    ListNode *head;
    ListNode node1=ListNode(1);
    ListNode node2=ListNode(2);
    ListNode node3=ListNode(3);
    ListNode node4=ListNode(4);
    head=&node1;
    node1.next=&node2;
    node2.next=&node3;
    node3.next=&node4;

    Solution S;
    ListNode *newhead2=S.reverseKFirst(head,3);
    ListNode *newhead1=S.reverseKGroup(head,2);
    cout << "Hello world!" << endl;
    return 0;
}
