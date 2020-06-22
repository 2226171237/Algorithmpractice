'''
输入一个字符串，打印出该字符串中字符的所有排列。
你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。

示例:
输入：s = "abc"
输出：["abc","acb","bac","bca","cab","cba"]

1 <= s 的长度 <= 8
'''

def getOne(s):
    # 从右往左找到第一个单增子序元素的第一个元素
    i=len(s)-1
    j=len(s)-2
    while j>=0:
        if s[i]<=s[j]:
            i-=1
            j-=1
        else:
            break
    return j if j>=0 else -1

def getTwo(s,i):
    # 取比 s[i]大，但是比它大的里面最小的元素，如果相同则取靠后的元素
    k=i+1
    mins=s[i+1]
    for j in range(i+2,len(s)):
        if s[j]>s[i] and s[j]<=mins: # 一定要小于等于，确保找到的还是最靠右的
            k=j
            mins=s[j]
    return  k
def reversed(s,low,high):
    while low<high:
        s[low],s[high]=s[high],s[low]
        low+=1
        high-=1

class Solution(object):
    def permutation(self,s):
        s=sorted(list(s))
        result=[''.join(s)]
        while True:
            i=getOne(s)
            if i<0:
                break
            else:
                k=getTwo(s,i)
                s[i],s[k]=s[k],s[i]
                reversed(s,i+1,len(s)-1)
                result.append(''.join(s))
        return result
    def permutation2(self, s):
        """
        这个只适合没有重复元素
        :type s: str
        :rtype: List[str]
        """
        result=[]
        def _permutation(s,i,path):
            if i>=len(s):
                result.append(''.join(path))
                return
            for j in range(i,len(s)):
                s[i],s[j]=s[j],s[i]
                path.append(s[i])
                _permutation(s,i+1,path)
                path.pop()
                s[i],s[j]=s[j],s[i]
        _permutation(list(s),0,[])
        return result

if __name__ == '__main__':
    S=Solution()
    result=S.permutation('kzfxxx')
    print(result)