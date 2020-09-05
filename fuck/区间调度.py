


from functools import cmp_to_key

def compare(a,b):
    if a[-1]>b[-1]:
        return 1
    else:
        return -1

def intervalSchedule(intvs):
    '''
    不相交的区间的最大个数，活动安排，你最多可以参见多少个活动?
    以 end 排序
    :param intvs: list[list[int]]
    :return: int
    '''
    intvs=sorted(intvs,key=cmp_to_key(compare))
    cnt=1
    end=intvs[0][-1]
    for intv in intvs[1:]:
        if intv[0]>=end:
            cnt+=1
            end=intv[-1]
    return cnt

print(intervalSchedule([[2,4],[1,3], [3,6]]))


