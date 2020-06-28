'''
请实现一个函数，把字符串 s 中的每个空格替换成"%20"。
'''
class Solution(object):
    def replaceSpace(self, s):
        """
        :type s: str
        :rtype: str
        """
        res=''
        for ch in s:
            if ch ==' ':
                res+='%20'
            else:
                res+=ch
        return  res