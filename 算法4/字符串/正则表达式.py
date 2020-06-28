

class DirectDFS:
    '''多源路径可达'''
    def __init__(self,G,s):
        s=s if isinstance(s,(list,tuple)) else [s]
        self._marked=[False for _ in range(len(G))]
        for x in s:
            if not self._marked[x]:
                self._dfs(G,x)

    def _dfs(self,G,x):
        self._marked[x]=True
        for y in G[x]:
            if not self._marked[y]:
                self._dfs(G,y)

    def hasPathTo(self,v):
        return self._marked[v]

class NFA:
    '''不确定有限状态机'''
    def __init__(self,regexp):
        self.re=regexp
        self.M=len(regexp)
        self.G=[[] for _ in range(self.M+1)] # 只记录e-转换
        stack=[]
        # lp: 左括号
        for i in range(self.M):
            lp=i
            if self.re[i] in '(|':
                stack.append(i)
            elif self.re[i]==')':
                oro=stack.pop()
                if self.re[oro]=='|':
                    lp=stack.pop()
                    self.G[lp].append(oro+1)
                    self.G[oro].append(i)
                else:
                    lp=oro
            if i<self.M-1 and self.re[i+1]=='*':
                self.G[lp].append(i+1)
                self.G[i+1].append(lp)
            if self.re[i] in '(*)':
                self.G[i].append(i+1)

    def recognizes(self,txt):
        '''识别'''
        pc=[] # 所有可能状态转换
        dfs=DirectDFS(self.G,0)

        for v in range(len(self.G)):
            if dfs.hasPathTo(v):
                pc.append(v)

        for i in range(len(txt)):
            match=[]
            for v in pc:
                if v<self.M:
                    if self.re[v]==txt[i] or self.re[v]=='.':
                        match.append(v+1)
            pc.clear()
            dfs=DirectDFS(self.G,match)
            for v in range(len(self.G)):
                if dfs.hasPathTo(v):
                    pc.append(v)
        for v in pc:
            if v==self.M:
                return True
        return False

if __name__ == '__main__':
    nfa=NFA('((A*B|AC)D)*')
    print(nfa.recognizes('BD'))


