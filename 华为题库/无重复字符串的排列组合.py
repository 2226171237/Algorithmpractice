'''
无重复字符串的排列组合。编写一种方法，计算某字符串的所有排列组合，字符串每个字符均不相同。

示例1:
 输入：S = "qwe"
 输出：["qwe", "qew", "wqe", "weq", "ewq", "eqw"]

示例2:
 输入：S = "ab"
 输出：["ab", "ba"]

提示:
字符都是英文字母。
字符串长度在[1, 9]之间。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutation-i-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:

    def getOne(self,s):
        i=len(s)-1
        j=len(s)-2
        while i>=0 and j>=0:
            if s[j]<=s[i]:
                return j
            i-=1
            j-=1
        return j
    def getNextNum(self,s,i):
        j=i+1
        maxs=s[j]
        mark=j
        while j<len(s):
            if s[j]<maxs and s[j]>s[i]:
                maxs=s[j]
                mark=j
            j+=1
        s[i],s[mark]=s[mark],s[i]
        ii=i+1
        jj=len(s)-1
        while ii<jj:
            s[ii],s[jj]=s[jj],s[ii]
            ii+=1
            jj-=1
        return s

    def permutation(self, S: str):

        result=[]
        S=sorted(S)
        result.append(''.join(S))
        while True:
            i=self.getOne(S)
            if i>=0:
                S=self.getNextNum(S,i)
                result.append(''.join(S))
            else:
                break
        return result

    def permutation2(self, S: str):
        '''
        递归
        :param S:
        :return:
        '''
        result=[]
        def _permutation(s:list,i,path:list):
            if i==len(s):
                result.append(''.join(path))
                return
            for j in range(i,len(s)):
                s[j],s[i]=s[i],s[j]
                path.append(s[i])
                _permutation(s,i+1,path)
                s[j], s[i] = s[i], s[j]
                path.pop()
        _permutation(list(S),0,[])
        return result

if __name__ == '__main__':
    S=Solution()
    print(S.permutation('123'))
    print(S.permutation2('123'))