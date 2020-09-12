'''
238: |2-3|=1 18: |1-8|=7(valid)
239: 8(NA)
532: 0(NA)
700: 7(valid)

howManyValidNum(1) = 1 (7)
howManyValidNum(2) = 6 (7 18 29 70 81 92)

(null)
0 1 2 3 4 5 6 7 8 9

shaoxuan.wsx@alibaba-inc.com

0XX

def howManyValidNum(rang):

def isValid(num):

    def getResult(num):
      	if 0<=num<=9:
          return num
        num,x=num//10,num%10
        return abs(getResult(num)-x)
    return getResult(num)==7
'''

def isValid(num):
    def getResult(num):
        if 0<=num<=9:
          return num
        num,x=num//10,num%10
        return abs(getResult(num)-x)
    return getResult(num)==7

def howManyValidNum(rang):
    cnt=[0]
    def dfs(i,num):
        if i==rang:
            return
        begin=0 if i>0 else 1
        for x in range(begin,10):
            t=abs(num-x)
            if t==7:
                cnt[0]+=1
            dfs(i+1,t)
    dfs(0,0)
    return cnt[0]

print(howManyValidNum(7))
