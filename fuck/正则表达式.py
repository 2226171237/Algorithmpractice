

def regress1(txt,p):
    '''完全匹配'''
    if len(p)==0:
        return len(txt)==0
    match= len(txt)>0 and txt[0]==p[0]
    return match and regress1(txt[1:],p[1:])

def regress2(txt,p):
    '''加入通配符 "." '''
    if len(p)==0:
        return len(txt)==0
    match=len(txt)>0 and p[0] in [txt[0],'.']
    return match and regress2(txt[1:],p[1:])


mem=dict()
def regress3(txt,p):
    '''加入通配符 "a*" '''
    if (txt,p) in mem:
        return mem[(txt,p)]
    if len(p)==0:
        return  len(txt)==0
    match =len(txt)>0 and p[0] in [txt[0],'.']
    if len(p)>1 and p[1]=='*':
        res=regress3(txt,p[2:]) or (match and regress3(txt[1:],p))
        mem[(txt,p)]=res
        return res
    res=match and regress3(txt[1:],p[1:])
    mem[(txt,p)]=res
    return res

print(regress3('aaabcdee','a*bc.e*'))
