import sys

# string=sys.stdin.readline().strip()
# string=list(string)
# result=[0]
# def permuite(string:str,i:int,path:list):
#     if i>len(string):
#         return
#     if i==len(string):
#         result[0]+=1
#     for j in range(i,len(string)):
#         string[i],string[j]=string[j],string[i]
#         path.append(string[i])
#         permuite(string,i+1,path)
#         path.pop()
#         string[i], string[j] = string[j], string[i]
#
# permuite(string,0,[])
# print(result[0])


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