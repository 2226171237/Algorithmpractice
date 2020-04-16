'''
找众数,线性时间复杂度。
'''

def majority(X):
    C=X[0]
    M=1
    for x in X[1:]:
        if M==0:
            C=x
            M=1
        else:
            M=M+1 if C==x else M-1
    if M==0:
        return -1
    else:
        count=0
        for x in X:
            if x==C:
                count+=1
        if count>len(X)/2:
            return C
        else:
            return -1

if __name__ == '__main__':

    X=[1,1,2,3,4,1,1,2,3,1,1,1,3,1,1,4]
    print(majority(X))
