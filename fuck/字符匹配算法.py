'''
BM算法  i=i+ (j-right[txt[i+j]])
'''

def find(txt,p):
    '''
    i=i+j-right(i+j)
    :param txt:
    :param p:
    :return:
    '''
    right=dict()
    for i,x in enumerate(p):
        right[x]=i
    i=0
    skip=1
    while i<=len(txt)-len(p):
        j=len(p)-1
        while j>=0:
            if txt[i+j]!=p[j]:
                r=right[txt[i+j]] if txt[i+j] in right else -1
                skip=max(1,j-r)
                break
            j-=1
        if j==-1:
            return i
        i+=skip
    return -1


print(find('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab','aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab'))

