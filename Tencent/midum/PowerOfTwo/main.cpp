#include <iostream>
/*
 * 给定一个整数，编写一个函数来判断它是否是 2 的幂次方。
示例 1:
输入: 1
输出: true
解释: 20 = 1
示例 2:
输入: 16
输出: true
解释: 24 = 16
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/power-of-two
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
 */

class Solution {
public:
    bool isPowerOfTwo(int n) {
        if (n<0) return false;
        int oneNum=0;
        while(n!=0)
        {
            oneNum++;
            n&=n-1;
        }
        return oneNum==1;
    }
};

int main() {
    std::cout << "Hello, World!" << std::endl;
    Solution s;
    std::cout<<s.isPowerOfTwo(218)<<std::endl;
    return 0;
}