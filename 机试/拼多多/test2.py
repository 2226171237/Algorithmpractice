'''
对N个筛子筛子分类。
每个筛子以 上下左右前后点数表示。如果俩个筛子可以通过旋转成一样表示，则他们是同一个筛子

直接暴力破解
'''

def up_down(point):
    # 绕上下轴旋转
    a1, a2, a3, a4, a5, a6 = point
    return [(a1, a2, a6, a5, a3, a4), (a1, a2, a4, a3, a6, a5), (a1, a2, a5, a6, a4, a3)]
def left_right(point):
    # 绕左右轴旋转
    a1, a2, a3, a4, a5, a6 = point
    return [(a6, a5, a3, a4, a1, a2), (a2, a1, a3, a4, a6, a5), (a5, a6, a3, a4, a2, a1)]

def front_back(point):
    # 绕前后轴旋转
    a1, a2, a3, a4, a5, a6 = point
    return [(a4, a3, a1, a2, a5, a6), (a2, a1, a4, a3, a5, a6), (a3, a4, a2, a1, a5, a6)]

def allPoints(point):
    # 枚举所有情况
    result=set()
    result.add(tuple(point))
    while True:
        temp=result.copy()
        for p in temp:
            for np in up_down(p)+left_right(p)+front_back(p):
                if np not in result:
                    result.add(np)
        if len(temp)==len(result):
            break
    return sorted(result)[0] # 返回排序第一个


def classifier(points):
    points=[allPoints(x) for x in points]
    result=dict()
    for p in points:
        result[p]=result.get(p,0)+1
    return list(result.values())

points=[[1,2,3,4,5,6],[1,2,3,4,6,5],[1,2,4,3,6,5],[1,2,4,3,5,6],[1,2,6,5,3,4],[1,2,5,6,4,3]]
print(classifier(points))

