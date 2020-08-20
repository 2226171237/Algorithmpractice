#include <iostream>
#include <vector>
#include <stack>

using namespace std;
/*
 * 给定一个二叉树，返回它的 前序 遍历。
 示例:
输入: [1,null,2,3]
   1
    \
     2
    /
   3
输出: [1,2,3]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-preorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
 */
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {

public:
    vector <int> preorderTraversal(TreeNode* root) {
        vector<int> result;
        preorder(root,result);
        return result;
    }
    void preorder(TreeNode *root,vector<int> &result)
    {
        if (NULL==root) return;
        result.push_back(root->val);
        preorder(root->left,result);
        preorder(root->right,result);
    }
    vector <int> preorderTraversal2(TreeNode* root) {
        vector<int> result;
        stack<TreeNode *> S;
        TreeNode *node;
        S.push(root);
        while(S.size()>0)
        {
            node=S.top();
            if (node!=NULL)
            {
                result.push_back(node->val);
                S.push(node->left);
            } else{
                S.pop();
                if (!S.empty())
                {
                    node=S.top();
                    S.pop();
                    S.push(node->right);
                }
            }
        }
        return result;
    }
};
int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}
