
class Solution:
    def compileSeq(self, input):
        input=[int(x) for x in input.split(',')]
        tree=dict()
        for i,x in enumerate(input):
            if x==-1:
                continue
            if x not in tree:
                tree[x]=[i]
            else:
                tree[x].append(i)
        non_parent=[]
        for i in range(len(input)):
            if i not in tree:
                non_parent.append(i)
        order=[]
        marked=[False for _ in range(len(input))]
        def dfs(s):
            marked[s]=True
            if s  not in tree:
                return
            for x in tree[s]:
                if not marked[x]:
                    dfs(x)
            order.append(s)
        for i in range(len(input)):
            if not marked[i] and i in tree:
                dfs(i)
        res=order[::-1]+non_parent
        return ','.join(map(str,res))

s=Solution()
print(s.compileSeq("1,2,-1,1"))