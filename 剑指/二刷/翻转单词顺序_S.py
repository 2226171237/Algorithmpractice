'''
输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。为简单起见，标点符号和普通字母一样处理。
例如输入字符串"I am a student. "，则输出"student. a am I"。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/fan-zhuan-dan-ci-shun-xu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

def reverse(arr,low,high):
   while low<high:
       arr[low],arr[high]=arr[high],arr[low]
       low+=1
       high-=1

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)==0:
            return ''
        arr=list(s)
        reverse(arr,0,len(arr)-1)
        s=''
        i=0
        while i<len(arr) and arr[i]==' ':
            i+=1
        j=i
        while j<len(arr):
            if arr[j]==' ':
                reverse(arr,i,j-1)
                s+=''.join(arr[i:j])+' '
                while j<len(arr) and arr[j]==' ':
                    j+=1
                i=j
            j+=1
        if arr[-1]==' ':
            return s[:-1]
        else:
            reverse(arr,i,j-1)
            s+=''.join(arr[i:j])
            return s


if __name__ == '__main__':
    s=Solution()
    print(s.reverseWords("   I am a student."))
