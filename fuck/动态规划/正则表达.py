

# 递归处理两个字符完全匹配
def isMatch(s,p):
    if len(p)==0:
        return len(s)==0
    first_match=len(s)>0 and p[0] in [s[0],'.']
    return first_match and isMatch(s[1:],p[1:])

# 处理"." 通配符
def isMatch2(s,p):
    if len(p)==0:
        return len(s)==0
    first_match=len(s)>0 and p[0] in [s[0],'.']
    return first_match and isMatch2(s[1:],p[1:])

# 处理"*" 通配符
def isMatch3(s,p):
    if len(p)==0:
        return len(s)==0
    first_match=len(s)>0 and p[0] in [s[0],'.']  # s==[] p!=[] 不一定不匹配，如 s='',p='.*0',也就是匹配0次的情况
    if len(p)>1 and p[1]=='*':
        A= isMatch3(s,p[2:]) # 匹配0次
        B= first_match and isMatch3(s[1:],p) # 匹配n次
        return A or B
    else:
        return  first_match and isMatch3(s[1:],p[1:])

print(isMatch3('aa','.*'))

# 记忆化，处理重复子问题
def isMatch4(s,p):
    mem=dict()
    def dp(i,j):
        if (i,j) in mem:
            return mem[(i,j)]
        if j==len(p):
            return i==len(s)
        first_match=i<len(s) and p[j] in [s[i],'.']
        if j+1<len(p) and p[j+1]=='*':
            A= dp(i,j+2) # 匹配0次
            B= first_match and dp(i+1,j) # 匹配n次
            res=A or B
        else:
            res=first_match and dp(i+1,j+1)
        mem[(i,j)]=res
        return res
    return dp(0,0)

print(isMatch4('aa','.*'))