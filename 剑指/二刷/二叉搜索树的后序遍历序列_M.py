'''
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。
如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。
'''
class Solution(object):
    def verifyPostorder(self, postorder):
        """
        :type postorder: List[int]
        :rtype: bool
        """
        if len(postorder)==0:
            return True
        root=postorder[-1]
        j=len(postorder)-1
        while j>=0 and postorder[j]>=root:
            j-=1

        for i in range(0,j):
            if postorder[i]>root:
                return False
        return self.verifyPostorder(postorder[:j+1]) and self.verifyPostorder(postorder[j+1:-1])

if __name__ == '__main__':
    s=Solution()
    print(s.verifyPostorder([1,3,2,6,5]))
