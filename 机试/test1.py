'''
有重复元素的字符串的排列问题
'''

def getone(string:list):
    i=len(string)-1
    j=len(string)-2
    while i>=0 and j>=0:
        if string[j]<string[i]:
            return j
        j-=1
        i-=1
    return j

def getTwo(string:list,i:int):
    if i<0:
        return
    maxs=string[i+1]
    k=i+1
    for j in range(i+1,len(string)):
        if string[j]<=maxs and string[j]>string[i]:
            maxs=string[j]
            k=j
    string[k],string[i]=string[i],string[k]
    ii=i+1
    jj=len(string)-1
    while ii<jj:
        string[ii],string[jj]=string[jj],string[ii]
        ii+=1
        jj-=1
    return string

def permuite2(string:str):
    string=list(string)
    string=sorted(string)
    result=1
    while True:
        i=getone(string)
        if i<0:
            return result
        else:
            string=getTwo(string,i)
            if string!=None:
                result+=1
            else:
                return result

string='aaabbb'
string=list(string)
print(permuite2(string))

class Solution:
    def __init__(self):
        self.cnt=0
    def permutation(self, S: str):
        self.cnt=0
        S=sorted(S)
        self.solve(S,[0 for _ in range(len(S))],[])
        return self.cnt

    def solve(self,S:list,flags:list,path:list):
        if len(path)==len(S):
            self.cnt+=1
            return
        for i in range(len(S)):
            if flags[i]==0:
                if i>0 and S[i]==S[i-1] and flags[i-1]==0:
                    continue
                path.append(S[i])
                flags[i]=1
                self.solve(S,flags,path)
                path.pop()
                flags[i]=0

S=Solution()
print(S.permutation('qqe'))


# def getOne(s):
#     i=len(s)-1
#     j=len(s)-2
#     while j>=0:
#         if s[i]<=s[j]:
#             i-=1
#             j-=1
#         else:
#             break
#     return j if j>=0 else -1
#
# def getTwo(s,i):
#     k=i+1
#     mins=s[i+1]
#     for j in range(i+2,len(s)):
#         if s[j]>s[i] and s[j]<=mins:
#             k=j
#             mins=s[j]
#     return  k
# def reversed(s,low,high):
#     while low<high:
#         s[low],s[high]=s[high],s[low]
#         low+=1
#         high-=1
#
# class Solution(object):
#     def permutation(self, s):
#         """
#         :type s: str
#         :rtype: List[str]
#         """
#         s=sorted(list(s))
#         result=[''.join(s)]
#         while True:
#             i=getOne(s)
#             if i<0:
#                 break
#             else:
#                 k=getTwo(s,i)
#                 s[i],s[k]=s[k],s[i]
#                 reversed(s,i+1,len(s)-1)
#                 result.append(''.join(s))
#         return result