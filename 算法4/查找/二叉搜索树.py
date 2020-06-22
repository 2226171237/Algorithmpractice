
from functools import lru_cache
class TreeNode:
    def __init__(self,key,val,left=None,right=None,N=1):
        self.key=key
        self.val=val
        self.left=left
        self.right=right
        self.N=N

class BST:
    def __init__(self):
        self.root=None

    def is_empty(self):
        return self.root is None

    def size(self):
        if self.is_empty():
            return 0
        else:
            return self.root.N

    @lru_cache(100)
    def get(self,key):
        def _get(root,key):
            if root==None:
                return None
            if root.key==key:
                return root.val
            elif root.key>key:
                return _get(root.left,key)
            else:
                return _get(root.right,key)
        return _get(self.root,key)

    def put(self,key,val):

        def _put(root,parent,key,val):
            if root==None:
                if parent.key>key:
                    parent.left=TreeNode(key,val)
                else:
                    parent.right=TreeNode(key,val)
                return
            if root.key>key:
                _put(root.left,root,key,val)
            elif root.key==key:
                root.val=val
            else:
                _put(root.right,root,key,val)
            N1=root.left.N if root.left else 0
            N2 = root.right.N if root.right else 0
            root.N=N1+N2+1

        if self.is_empty():
            self.root=TreeNode(key,val)
        else:
            root=self.root
            _put(root,root,key,val)

    @lru_cache(20)
    def select(self,k):
        '''
        选择排名为k的键
        :param k:
        :return:
        '''

        def _select(root,k):
            if root==None:
                return None
            nums=root.left.N if root.left else 0
            nums+=1 #左子树加根结点的结点个数
            if nums>k:
                return _select(root.left,k)
            elif nums==k:
                return root.key
            else:
                return _select(root.right,k-nums)

        if k>self.size() or k<1:
            raise ValueError
        else:
            return _select(self.root,k)

    def rank(self,key):
        # 返回key的排名
        def _rank(root,key):
            if root==None:
                return 0
            if root.key>key:
                return _rank(root.left,key)
            elif root.key==key:
                return root.left.N if root.left else 0
            else:
                n=root.left.N+1 if root.left else 1
                return n+_rank(root.right,key)
        return _rank(self.root,key)

    @lru_cache(10)
    def Min(self):
        '''
        返回最小键
        :return:
        '''
        if self.is_empty():
            return None
        node=self.root
        parent=node
        while node:
            parent=node
            node=node.left
        return parent.key

    def delMin(self):
        '''
        删除最小键
        :return:
        '''
        def _delMin(root):
            if root.left==None:
                return root.right
            root.left=_delMin(root.left)
            n1=root.left.N if root.left else 0
            n2 = root.right.N if root.right else 0
            root.N=n1+n2+1
            return root
        self.root=_delMin(self.root)

    def delete(self,key):
        '''
        删除指定键
        :param key:
        :return:
        '''
        def _Min(root):
            if self.is_empty():
                return None
            node = root
            parent = node
            while node:
                parent = node
                node = node.left
            return parent

        def _delMin(root):
            if root.left==None: return root.right
            root.left=_delMin(root.left)
            n1=root.left.N if root.left else 0
            n2 = root.right.N if root.right else 0
            root.N=n1+n2+1
            return root

        def _delete(root,key):
            if root==None:  return root
            if root.key==key:
                # 单子结点情况
                if root.right==None: return root.left
                if root.left==None:  return root.right
                # 双子节点情况
                node=_Min(root.right)
                node.right=_delMin(root.right)
                node.left=root.left
                return node
            elif root.key>key:
                root.left=_delete(root.left,key)
            else:
                root.right=_delete(root.right,key)
            n1 = root.left.N if root.left else 0
            n2 = root.right.N if root.right else 0
            root.N=n1+n2+1
            return root

        self.root=_delete(self.root,key)

    def keys(self,low_key,high_key):
        # 返回low_key和high_key之间的key，包含边界
        result=[]
        def _keys(root,low,high):
            if root==None:
                return
            if root.key<low:
                _keys(root.right,low,high)
            if low<=root.key<=high:
                _keys(root.left,low,high)
                result.append(root.key)
                _keys(root.right,low,high)
            if root.key>high:
                _keys(root.left,low,high)
        _keys(self.root,low_key,high_key)
        return result

if __name__ == '__main__':
    st=BST()
    keys=list('aefsjga')
    vals=[1,2,3,4,5,6,7]
    for key,val in zip(keys,vals):
        st.put(key,val)
    for key in keys:
        print(st.get(key))
    print(st.size())
    print(st.select(2))
    print(st.rank('f'))
    st.delete('s')
    for key in keys:
        print(st.get(key))
    print(st.keys('a','h'))