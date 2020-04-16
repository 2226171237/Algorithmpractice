'''
如何找到由其他单词组成的最长单词？
给定一个字符串数组，找出数组中最长的字符串，使其能由数组中其他字符串组成。
如：给定字符串数组['test','tester','testertest','testing','apple','seattle','banana','batting','ngcat',
'batti','bat','testingtester','testbattingcat'] 满足的字符串为‘testbattingcat’
'''


def isHave(s,L,lens):
    if len(s)==0:
        return True
    i=1
    while i<=len(s):
        if i==lens:
            return False
        flag=False
        for x in L:
            if x==s[0:i]:
                flag=True
                break
        if flag:
            if isHave(s[i:],L,lens):
                return True
        i+=1
    return False

def find(L):
    i=0
    n=len(L)
    while i<n-1:
        j=i+1
        while j<n:
            if len(L[i])<len(L[j]):
                t=L[i]
                L[i]=L[j]
                L[j]=t
            j+=1
        i+=1

    for x in L:
        if isHave(x,L,len(x)):
            return x
    return False

if __name__ == '__main__':
    L=['test', 'tester', 'testertest', 'testing', 'apple', 'seattle', 'banana', 'batting', 'ngcat',
     'batti', 'bat', 'testingtesterass', 'testbattingcat']
    print(find(L))
    print(L)