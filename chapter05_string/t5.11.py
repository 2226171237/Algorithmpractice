'''
如何按照给定的字母序列对字符数组排序
已知字母序列[d,g,e,c,f,b,o,a],请实现一个方法，要求对输入的一组字符串
['bed','dog','dear','eye']按照字母顺序排序并打印。输出为['dear','dog',,'eye','bed']
'''

def compare(s1,s2,d):
    n1=len(s1)
    n2=len(s2)
    i=0
    while i<n1 and i<n2 and d[s1[i]]==d[s2[i]]:
        i+=1
    if i==n1:
        if n1==n2:
            return 0
        elif n1<n2:
            return -1
        else:
            return 1
    elif d[s1[i]]>d[s2[i]]:
        return 1
    else:
        return -1

def sorted(L,g):
    i=0
    d={x:i for i,x in enumerate(g)}
    n=len(L)
    while i<n-1:
        j=i+1
        while j<n:
            if compare(L[i],L[j],d)>0:
                t=L[i]
                L[i]=L[j]
                L[j]=t
            j+=1
        i+=1
    return L

if __name__ == '__main__':
    L=['bed', 'dog', 'dear', 'eye']
    g=['d','g','e','c','f','b','o','a']
    print(sorted(L,g))