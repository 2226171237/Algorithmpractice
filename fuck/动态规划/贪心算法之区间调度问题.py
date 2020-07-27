
# 区间合并问题，区间 [start,end]
# 对区间按章start 升序排序，然后从左到右依次合并

from functools import cmp_to_key


def merge(inves):
    def compare(a, b):
        if a[0] > b[0]:
            return 1
        else:
            return -1
    inves=sorted(inves,key=cmp_to_key(compare))
    result=[inves[0]]
    for x2,y2 in inves[1:]:
        x1,y1=result[-1]
        if x1<x2<y1: # 合并
            result.pop()  # 要弹出
            x=min(x1,x2)
            y=max(y1,y2)
            result.append([x,y])
        else:
            result.append([x2,y2])
    return result

print(merge([[0,4],[4,5],[2,4],[6,8]]))


# 最大不相交区间数,按end排序
def intervalSchedule(inves):
    def compare(a, b):
        if a[1] > b[1]:
            return 1
        else:
            return -1
    inves=sorted(inves,key=cmp_to_key(compare))
    cnt=1
    x_end=inves[0][1]
    for v in inves:
        start,end=v
        if start>=x_end:
            cnt+=1
            x_end=end
    return cnt

print(intervalSchedule([[0,4],[4,5],[2,4],[6,8]]))

