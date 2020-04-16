#-*-coding=utf-8-*-
'''
如何让求解最小三元组距离？
已知三个升序整数数组，a[l],b[m],c[n],请在三个数组中各找出一个元素，使得组成的三元组距离最小。
三元组距离定义为：假设a[i],b[j]和c[k]是一个三元组，那么距离为 max(|a[i]-b[j]|,|a[i]-c[k]|,|b[j]-c[k]|)
'''
# 蛮力法
def findMaxDistance1(a,b,c):
    _Min=max(abs(a[0]-b[0]),abs(a[0]-c[0]),abs(b[0]-c[0]))
    for x in a:
        for y in b:
            for z in c:
                t=max(abs(x-y),abs(x-z),abs(y-z))
                if t<_Min:
                    _Min=t
    return _Min

# 最小距离法
def findMaxDistance2(a,b,c):
    # a,b,c必须为升序
    a_t=[0,0,0]
    _Min=max(abs(a[0]-b[0]),abs(a[0]-c[0]),abs(b[0]-c[0]))
    def argmin(x):
        x=[a[x[0]],b[x[1]],c[x[2]]]
        min=x[0]
        index=0
        for i,d in enumerate(x):
            if d<min:
                min=d
                index=i
        return index
    lens=[len(a),len(b),len(c)]
    while True:
        index=argmin(a_t)
        a_t[index]+=1
        if a_t[index]<lens[index]:
            t=max(abs(a[a_t[0]]-b[a_t[1]]),abs(a[a_t[0]]-c[a_t[2]]),abs(b[a_t[1]]-c[a_t[2]]))
            if t<_Min:
                _Min=t
        else:
            return _Min

# 数学运算法
#max(|a-b|,|a-c|,|b-c|)=1/2*(|a-b|+|a-c|+|b-c|)
#然后使用上面的方法
if __name__ == '__main__':
    import random
    a=[1,2,3,4,5,6,7,15,16,17,18]
    b=[10,12,14,16,17,18,19,20]
    c=[20,21,23,24,37,38]

    print(findMaxDistance1(a,b,c))
    print(findMaxDistance2(a, b, c))