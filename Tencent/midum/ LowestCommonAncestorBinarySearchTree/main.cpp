/*
 * 给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。
百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
例如，给定如下二叉搜索树:  root = [6,2,8,0,4,7,9,null,null,3,5]
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
 */
#include <iostream>


struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if(root==NULL) return NULL;
        if(root==p) return p;
        if (root==q) return q;
        int minVal=p->val>q->val?q->val:p->val;
        int maxVal=p->val>q->val?p->val:q->val;
        if(maxVal<root->val)
            return lowestCommonAncestor(root->left,p,q);
        else if (minVal>root->val)
            return lowestCommonAncestor(root->right,p,q);
        else
        {
            TreeNode *A=lowestCommonAncestor(root->left,p,q);
            TreeNode *B=lowestCommonAncestor(root->right,p,q);
            if (A!=NULL && B!=NULL)
                return root;
            else
                return A!=NULL?A:B;
        }
    }
};

int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}
