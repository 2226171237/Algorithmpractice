/*
 * 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。
 * 返回这三个数的和。假定每组输入只存在唯一答案。
示例：
输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
提示：
3 <= nums.length <= 10^3
-10^3 <= nums[i] <= 10^3
-10^4 <= target <= 10^4
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum-closest
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
 */
#include <iostream>
#include <vector>
#include <algorithm>

using  namespace std;

class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        sort(nums.begin(),nums.end());
        int i,left,right;
        int sum,res;
        int dis=INT32_MAX;
        for(i=0;i<nums.size()-2;i++)
        {
            left=i+1;
            right=nums.size()-1;
            while (left<right)
            {
                sum=nums[i]+nums[left]+nums[right];
                if (abs(sum-target)<dis)
                {
                    res=sum;
                    dis=abs(sum-target);
                }
                if (sum==target)
                    return sum;
                else if(sum>target)
                    right-=1;
                else
                    left+=1;
            }
        }
        return res;
    }
};

int main() {
    vector<int> nums={1,1,1,0};
    Solution s;
    std::cout<<s.threeSumClosest(nums,10)<<std::endl;
    std::cout << "Hello, World!" << std::endl;
    return 0;
}
