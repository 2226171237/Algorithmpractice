
class LinearProbingHashST:
    '''
    线性探索散列表
    '''
    def __init__(self,M=16):
        self.N=0
        self.M=M
        self._keys=[None for _ in range(self.M)]
        self._vals=[None for _ in range(self.M)]

    def resize(self,cap):
        tmpST=LinearProbingHashST(cap)
        for i,key in enumerate(self._keys):
            if key:
                tmpST.put(key,self._vals[i])
            else:
                continue
        self._keys=tmpST._keys
        self._vals=tmpST._vals
        self.M=tmpST.M

    def hash_map(self,key):
        return (hash(key)&0x7fffffff)%self.M

    def put(self,key,val):
        if self.N>=self.M//2:
            self.resize(2*self.M)
        i=self.hash_map(key)
        while self._keys[i]:
            if self._keys[i]==key:
                self._vals[i]=val
                return
            i=(i+1)%self.M
        self._keys[i]=key
        self._vals[i]=val
        self.N+=1

    def get(self,key):
        i=self.hash_map(key)
        while self._keys[i]:
            if self._keys[i]==key:
                return self._vals[i]
            i=(i+1)%self.M
        raise KeyError

    def contains(self,key):
        i = self.hash_map(key)
        while self._keys[i] != key and self._keys[i]:
            i = (i + 1) % self.M
        if self._keys[i] == None:
            return False
        else:
            return True

    def delete(self,key):
        i=self.hash_map(key)
        while self._keys[i]!=key and self._keys[i]:
            i=(i+1)%self.M
        if self._keys[i]==None:
            raise KeyError
        self._keys[i]=None
        self.N-=1
        i=(i+1)%self.M
        while self._keys[i]:
            key,val=self._keys[i],self._vals[i]
            self._keys[i]=None
            self.N-=1
            self.put(key,val)
            i=(i+1)%self.M
        if 0<self.N and self.N==self.M//8:
            self.resize(self.M//2)


if __name__ == '__main__':
    d=LinearProbingHashST()
    keys=list('abcdeftgjsi')
    vals=[1,2,3,4,5,6,7,8,9,10,11]
    for key,val in zip(keys,vals):
        d.put(key,val)
    for key in keys:
        print(key,':',d.get(key),end='; ')
    print()

    d.delete('s')
    for key in keys:
        if d.contains(key):
            print(key,':',d.get(key),end='; ')
    print()






