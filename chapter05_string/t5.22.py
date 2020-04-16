'''
如何求相对路径？
编写一个函数，根据两个文件的绝对路径算出其相对路径。例如：
a='/qihoo/app/a/b/c/d/new.c',b='/qihoo/app/1/2/test.c'，那么b相对a的相对路径是'../../../../1/2/test.c'
'''

def getPath(a,b):
    n1=len(a)
    n2=len(b)
    i=0
    k=0
    path=''
    while i<n1 and i<n2:
        if a[i]==b[i]:
            if a[i]=='/':
                k=i
            i+=1
        else:
            ii=k+1
            while ii<n1:
                if a[ii]=='/':
                    path+='../'
                ii+=1
            path+=b[k+1:]
            break
    return path


if __name__ == '__main__':
    a = '/qihoo/app/1/2/c/d/new.c'
    b = '/qihoo/app/1/2/test.c'
    print(getPath(a,b))

