'''
回溯法：N皇后问题
'''

def isValid(nums,row):
    for i in range(row):
        if abs(row-i)==abs(nums[i]-nums[row]) or nums[i]==nums[row]:
            return False
    else:
        return True

def dfs(nums,i,result):
    if i==len(nums):
        result.append(nums[:])
        return
    for col in range(len(nums)):
        nums[i]=col
        if isValid(nums,i):
            dfs(nums,i+1,result)


def solver(N):
    nums=[None for _ in range(N)]
    result=[]
    dfs(nums,0,result)
    for m in result:
        for col in m:
            t=['*' for _ in range(N) ]
            t[col]='Q'
            print(t)
        print()

solver(8)