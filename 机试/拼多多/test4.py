
import sys

grid=[]
for _ in range(6):
    grid.append(list(sys.stdin.readline().strip()))

empty_nums=0
seed_map=dict()
for i in range(6):
    for j in range(6):
        if grid[i][j]=='#':
            empty_nums+=1
            seed_map[(i,j)]=0


marked=[[False for _ in range(6)] for _ in range(6)]

def axvalid(i,j):
    return i>=0 and i<6 and j>=0 and j<6

def isValid(i,j):
    return  axvalid(i,j) and not marked[i][j]

def seedValid(i,j,seed):
    if axvalid(i-1,j) and grid[i-1][j]=='#':
        if seed_map[(i-1,j)]==seed:
            return False
    if axvalid(i,j-1) and grid[i][j-1]=='#':
        if seed_map[(i,j-1)]==seed:
            return False
    if axvalid(i+1,j) and grid[i+1][j]=='#':
        if seed_map[(i+1,j)]==seed:
            return False
    if axvalid(i,j+1) and grid[i][j+1]=='#':
        if seed_map[(i,j+1)]==seed:
            return False
    return True

cnts=[0]
def dfs(i,j,nums):
    if nums==empty_nums:
        cnts[0]+=1
        return
    if not isValid(i,j):
        return
    marked[i][j] = True
    if grid[i][j]=='#':
        for seed in range(1,7):
            if seedValid(i,j,seed) and seed_map[(i,j)]==0:
                seed_map[(i,j)]=seed
                dfs(i+1,j,nums+1)
                dfs(i-1,j,nums+1)
                dfs(i,j+1,nums+1)
                dfs(i,j-1,nums+1)
                seed_map[(i,j)]=0
    else:
        dfs(i + 1, j, nums)
        dfs(i - 1, j, nums)
        dfs(i, j + 1, nums)
        dfs(i, j - 1, nums)
    marked[i][j]=False

dfs(0,0,0)

print(cnts[0])

