'''
着色问题，算法引论 6.9
'''
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

class Elem:
    def __init__(self,id,point):
        self.id=id
        self.x=point.x
        self.y=point.y
        self.color=None
        self.subSets=[] # 所属的子集

class SubSet:
    def __init__(self,id):
        self.id=id
        self.state=3      # 0: 里面有红也有蓝，1：红子集，2：蓝子集，3：中性子集
        self.no_color_elems=0

def cal_FR(S,x):
    # x如果着红色，n-1个元素的无效着色概率
    P=0
    for i,s in enumerate(S):
        if i in x.subSets:
            if s.state==1:
                if s.no_color_elems>1:
                    P+=2**(-s.no_color_elems)
                else:
                    P+=1
            elif s.state==2:
                continue
            elif s.state==3:
                if s.no_color_elems>1:
                    P+=2**(-s.no_color_elems+1)
                else:
                    P+=1
    return P

def cal_FB(S,x):
    # x如果着蓝色，n-1个元素的无效着色概率
    P = 0
    for i, s in enumerate(S):
        if i in x.subSets:
            if s.state == 1:
                continue
            elif s.state == 2:
                if s.no_color_elems > 1:
                    P += 2 ** (-s.no_color_elems)
                else:
                    P += 1
            elif s.state == 3:
                if s.no_color_elems > 1:
                    P += 2 ** (-s.no_color_elems + 1)
                else:
                    P += 1
    return P

def updateS(S,x):
    c=x.color
    for i in x.subSets:
        S[i].no_color_elems-=1
        if S[i].state==1:
            if c=='b':
                S[i].state=0
        elif S[i].state==2:
            if c=='r':
                S[i].state=0
        elif S[i].state==3:
            if c=='r':
                S[i].state=1
            else:
                S[i].state=2

def setColor(X,S):
    # 着色
    for x in X:
        FR=cal_FR(S,x)
        FB=cal_FB(S,x)
        if FB<FR:
            x.color='b'
        else:
            x.color='r'
        updateS(S,x)


if __name__ == '__main__':
    import  random
    x=[random.randint(0,10) for _ in range(10)]
    y=[random.randint(0,10) for _ in range(10)]
    X=[Elem(i,Point(x_,y_)) for i,(x_,y_) in enumerate(zip(x,y))]
    X[0].subSets=[0]
    X[1].subSets=[0,1]
    X[2].subSets=[0,1]
    X[3].subSets=[1,3]
    X[4].subSets=[1,2]
    X[5].subSets=[0,3]
    X[6].subSets=[2]
    X[7].subSets=[2]
    X[8].subSets=[3,2]
    X[9].subSets=[3]
    S=[SubSet(i) for i in range(4)]
    S[0].no_color_elems=4
    S[1].no_color_elems=4
    S[2].no_color_elems=4
    S[3].no_color_elems=4

    setColor(X,S)
    colors=[x.color for x in X]
    print(x)
    print(y)
    print(colors)


