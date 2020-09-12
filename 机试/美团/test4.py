

def isValid(a):
    a=sorted(a)
    def dfs(a):
        if len(a)==0 and a[0]==1:
            return True
        if a[-1]!=sum(a[:-1])+1:
            if a[-1]==1:
                return dfs(a[:-1])
            else:
                return False
        else:
            return True
    return dfs(a)

def havesubtree(tree,a,x):
    indexs=list(tree)
    for i in range(len(indexs)-1):
        for j in range(i+1,len(indexs)):
            if a[indexs[i]]+a[indexs[j]]+1==x:
                return indexs[i],indexs[j]
    return -1,-1

def isValid2(a):
    a=sorted(a)
    def dfs(i,tree):
        if i==len(a):
            return len(tree)==1
        if len(tree) == 0:
            if a[i] == 1:
                tree.add(i)
            else:
                return False
        elif a[i] == 1:
            tree.add(i)
        else:
            ii, jj = havesubtree(tree, a, a[i])
            if ii == -1:
                return False
            else:
                tree.remove(ii)
                tree.remove(jj)
                tree.add(i)
        return dfs(i+1,tree)
    return dfs(0,set())

print(isValid2([1,1,1,3,4]))
# import sys
# n=sys.stdin.readline().strip()
# while len(n)>0:
#     a=[int(x) for x in sys.stdin.readline().strip().split(' ')]
#     if isValid2(a):
#         print('YES')
#     else:
#         print('NO')
#     n = sys.stdin.readline().strip()

# 答案
def isValidTree(a):
    a=sorted(a,reverse=True)  # 每个结点剩下多少个总子结点没有分配
    child=[0 for _ in range(len(a))] # 每个结点已分配了多少个子结点
    cand=set() # : 所有没有分配的结点，a[i]>1的结点
    cand.add(0)
    def dfs(i,cand):
        if i==len(a):
            for i in range(len(a)):
                if a[i]!=1 or child[i]==1:
                    return False
            return True
        new_cand=cand.copy()
        if a[i]!=1:
            new_cand.add(i)
        for j in cand:
            if a[j]==a[i]+1 and child[i]==0: continue
            a[j]-=a[i]
            child[j]+=1
            if a[j]==1:  # arr[j]=1因为最后只剩下自己没分配出去。
                new_cand.remove(j)
            if dfs(i+1,new_cand): return True
            if a[j]==1:
                new_cand.add(j)
            a[j]+=a[i]
            child[j]-=1
        return False
    return dfs(1,cand)