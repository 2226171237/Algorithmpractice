'''
以 Unix 风格给出一个文件的绝对路径，你需要简化它。或者换句话说，将其转换为规范路径。
在 Unix 风格的文件系统中，一个点（.）表示当前目录本身；此外，两个点 （..） 表示将目录切换到上一级（指向父目录）；
两者都可以是复杂相对路径的组成部分。更多信息请参阅：Linux / Unix中的绝对路径 vs 相对路径

请注意，返回的规范路径必须始终以斜杠 / 开头，并且两个目录名之间必须只有一个斜杠 /。最后一个目录名（如果存在）不能以 / 结尾。
此外，规范路径必须是表示绝对路径的最短字符串。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/simplify-path
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """

        sPath=[]
        i=0
        while i<len(path):
            while i<len(path) and path[i]=='/':
                i+=1
            dir=''
            while i<len(path) and path[i]!='/':
                dir+=path[i]
                i+=1
            if dir=='..':
                if sPath:
                    sPath.pop()
            elif dir=='.':
                continue
            elif dir:
                sPath.append(dir)
        return '/'+'/'.join(sPath)

if __name__ == '__main__':
    s=Solution()
    print(s.simplifyPath('/a/../../b/../c//.//'))