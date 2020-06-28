

def keyIndexSort(arr,R):
    '''键索引计数法(小整数排序)'''
    aux=arr.copy()
    count=[0 for _ in range(R+1)]
    for val,key in arr:
        count[key+1]+=1
    for i in range(1,R+1):
        count[i]+=count[i-1]

    for val,key in arr:
        aux[count[key]]=(val,key)
        count[key]+=1

    for i in range(len(aux)):
        arr[i]=aux[i]


class LSD:
    '''低位优先的字符串排序'''
    def sort(self,arr,w):
        '''
        :param  list[str] arr: 字符串列表
        :param  int w: 字符串长度
        :return:
        '''
        N=len(arr)
        R=256
        aux=arr.copy()
        for d in range(w-1,-1,-1):
            count=[0 for _ in range(R+1)]
            for x in arr:
                count[ord(x[d])+1]+=1
            for r in range(1,R+1):
                count[r]+=count[r-1]

            for i in range(N):
                key=ord(arr[i][d])
                aux[count[key]]=arr[i]
                count[key]+=1

            for i in range(N):
                arr[i]=aux[i]

class InsertSort:
    def sort(self,arr,low,high,d):
        for i in range(low,high+1):
            for j in range(i,low,-1):
                if arr[j][d:]<arr[j-1][d:]:
                    arr[j-1],arr[j]=arr[j],arr[j-1]
class MSD:
    '''高位优先排序'''
    def __init__(self):
        self.R=256
        self.H=10
        self.insertsort=InsertSort()
    def sort(self,arr):
        self.aux=arr.copy()
        self.subsort(arr,0,len(arr)-1,0)

    def key(self,s,d):
        if d>=len(s):
            return -1
        return ord(s[d])

    def subsort(self,arr,low,high,d):
        if high<=low+self.H:
            self.insertsort.sort(arr,low,high,d)
            return
        counts=[0 for _ in range(self.R+2)]
        for i in range(low,high+1):
            key=self.key(arr[i],d)
            counts[key+2]+=1

        for r in range(1,self.R+2):
            counts[r]+=counts[r-1]

        for i in range(low,high+1):
            key=self.key(arr[i],d)
            self.aux[counts[key+1]]=arr[i]
            counts[key+1]+=1

        for i in range(low,high+1):
            arr[i]=self.aux[i-low]

        for r in range(0,self.R):
            self.subsort(arr,low+counts[r],low+counts[r+1]-1,d+1)


class Quick3string:
    '''三向切分字符串快排'''
    def key(self,s,d):
        if len(s)<=d:
            return -1
        else:
            return ord(s[d])

    def sort(self,arr):
        self._subsort(arr,0,len(arr)-1,0)

    def _subsort(self,arr,low,high,d):
        if low>=high:
            return
        v=self.key(arr[low],d)
        lt=low
        i=low+1
        gt=high
        while i<=gt:
            t=self.key(arr[i],d)
            if t<v:
                arr[i],arr[lt]=arr[lt],arr[i]
                i+=1
                lt+=1
            elif t==v:
                i+=1
            else:
                arr[i],arr[gt]=arr[gt],arr[i]
                gt-=1
        self._subsort(arr,low,lt-1,d)
        if v>0:
            self._subsort(arr,lt,gt,d+1)
        self._subsort(arr,gt+1,high,d)

if __name__ == '__main__':
    arr=[('lijie',1),('liuzi',2),('zhangliu',2),('miwmi',1),('liuzhao',3),('xiaozju',2),('liejo',3),('liuzhao',0)]
    keyIndexSort(arr,4)
    print(arr)

    arr=['4PGC938','2IYE230','3CI0720','1ICK750','10HV845','4JZY524','1ICK750','3CI0720','10HV845']
    s=LSD()
    s.sort(arr,7)

    s=MSD()
    arr=['she','by','shells','the','sea','are','surely','seashells']
    s.sort(arr)
    print(arr)

    qs=Quick3string()
    arr = ['she', 'by', 'shells', 'the', 'sea', 'are', 'surely', 'seashells']
    qs.sort(arr)
    print(arr)


