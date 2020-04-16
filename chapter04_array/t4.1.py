#-*-coding=utf-8-*-
'''
如何找出数组中唯一得重复元素。
数字1-1000，放在含有1001个元素得数组中，其中只有唯一得一个元素重复，其他数字均只出现一次。
设计一个算法，将重复元素找出来，要求每个数组元素只能访问一次。如果步使用辅助控件，你能否设计一个算法？
'''

# 方法1：hash set
def findDup(arr):
    hash_set=set()
    for x in arr:
        if x not in hash_set:
            hash_set.add(x)
        else:
            return x

# 方法2：累加求和
def findDup2(arr):
    sum=0
    for i in arr:
        sum+=i
    return sum-int((1+1000)*1000/2)

# 方法3： 异或法
def findDup3(arr):
    xor=0
    for i,x in enumerate(arr[:-1]):
        xor^=x
        xor^=i+1
    xor^=arr[-1]
    return xor

# 方法4：数据映射法
def findDup4(arr):
    bef=0
    aft=arr[0]
    while aft>=0:
        arr[bef] *= -1
        bef = aft
        aft=arr[aft]
    return bef

# 引申：对于一个给定得自然数N，有一个N+M个元素的数组，
# 其中存放了小于等于N的所有自然数，求重复出现的自然数序列{X}
def findDup5(arr,num):
    s=set()
    if None==arr:
        return s
    lens=len(arr)
    index=arr[0]
    num=num-1
    while True:
        if arr[index]<0:
            num-=1
            arr[index]=lens-num
            s.add(index)
        if 0==num:
            return s
        arr[index]*=-1
        index=arr[index]*(-1)

if __name__ == '__main__':
    import random
    arr=[]
    for i in range(1,1001,1):
        arr.append(i)
    x=random.randint(1,1001)
    arr.append(x)
    random.shuffle(arr)
    print(x,findDup(arr))
    print(x, findDup2(arr))
    print(x, findDup3(arr))
    print(x, findDup4(arr))
    arr=[1,2,3,3,3,4,5,5,5,6]
    print(x,findDup5(arr,6))

