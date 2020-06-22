
class BinarySearchST:
    '''二分搜索查找'''
    def __init__(self):
        self._keys=[]
        self._values=[]

    def is_empty(self):
        return len(self._keys)==0

    def keys(self):
        return self._keys

    def values(self):
        return self._values

    def rank(self,key):
        # 找到比key小的key的个数
        low=0
        high=len(self._keys)-1
        while low<=high:
            mid=(low+high)//2
            if self._keys[mid]>key:
                high=mid-1
            elif self._keys[mid]<key:
                low=mid+1
            else:
                return mid
        return low

    def put(self,key,val):
        idx=self.rank(key)
        if idx<len(self._keys) and  self._keys[idx]==key:
            self._values[idx]=val
        else:
            self._keys.insert(idx,key)
            self._values.insert(idx,val)

    def get(self,key):
        idx=self.rank(key)
        if idx<len(self._keys) and self._keys[idx]==key:
            return self._values[idx]
        else:
            return None

    def delete(self,key):
        idx=self.rank(key)
        if idx<len(self._keys) and self._keys[idx]==key:
            self._keys.pop(idx)

if __name__ == '__main__':
    st=BinarySearchST()
    keys=list('aefsjgc')
    vals=[1,2,3,4,5,6,7]
    for key,val in zip(keys,vals):
        st.put(key,val)
    for key in keys:
        print(st.get(key))