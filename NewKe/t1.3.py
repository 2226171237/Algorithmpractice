'''
产品经理(PM)有很多好的idea，而这些idea需要程序员实现。现在有N个PM，在某个时间会想出一个 idea，
每个 idea 有提出时间、所需时间和优先等级。对于一个PM来说，最想实现的idea首先考虑优先等级高的，
相同的情况下优先所需时间最小的，还相同的情况下选择最早想出的，没有 PM 会在同一时刻提出两个 idea。

同时有M个程序员，每个程序员空闲的时候就会查看每个PM尚未执行并且最想完成的一个idea,然后从中挑选出
所需时间最小的一个idea独立实现，如果所需时间相同则选择PM序号最小的。直到完成了idea才会重复上述操
作。如果有多个同时处于空闲状态的程序员，那么他们会依次进行查看idea的操作。

求每个idea实现的时间。

输入第一行三个数N、M、P，分别表示有N个PM，M个程序员，P个idea。随后有P行，每行有4个数字，分别是PM
序号、提出时间、优先等级和所需时间。输出P行，分别表示每个idea实现的时间点。
'''
class Idea:
    def __init__(self,id,PM_index,startTime,prior,needTimes):
        self.id=id
        self.PM_index=PM_index
        self.startTime=startTime
        self.prior=prior
        self.needTimes=needTimes

    def __str__(self):
        return '(%d %d %d %d %d)' % (self.id,self.PM_index,self.startTime,self.prior,self.needTimes)

class ProductManger:
    def __init__(self,id):
        self.id=id
        self.ideas=[]

    def add_idea(self,idea):
        self.ideas.append(idea)

    def is_empty(self):
        return len(self.ideas)==0

    def popIdea(self,i):
        self.ideas.pop(i)

    def nextIdea(self,t):
        thisIdea=self.ideas[0]
        ind=0
        for i,idea in enumerate(self.ideas):
            if idea.startTime<=t:
                if idea.prior>thisIdea.prior:
                    thisIdea=idea
                    ind=i
                elif idea.prior==thisIdea.prior:
                    if idea.needTimes<thisIdea.needTimes:
                        thisIdea = idea
                        ind = i
                    elif idea.needTimes==thisIdea.needTimes:
                        if idea.startTime<thisIdea.startTime:
                            thisIdea = idea
                            ind = i
        if thisIdea.startTime>t:
            return None,-1
        else:
            return thisIdea,ind

class Coder:
    def __init__(self,id):
        self.id=id
        self.workerState=False
        self.TaskTimes=0
        self.startTime=-1
        self.systemTime=0

    def getState(self):
        return self.workerState

    def setWorkState(self,state):
        self.workerState=state

    def updateState(self):
        self.workerState=(self.systemTime-self.startTime)!=self.TaskTimes and self.startTime!=-1


def solver(N,M,P):
    # N个PM，M个Coder,P个idea
    PM=[ProductManger(i) for i in range(N)]
    Coders=[Coder(i) for i in range(M)]
    IdeaStartTimes=[None for i in range(len(P))]
    for i,idea in enumerate(P):
        idea=Idea(i,*idea)
        PM[idea.PM_index-1].add_idea(idea)
    i=0
    ideaNums=len(P)
    while i<ideaNums:
        for coder in Coders:
            if coder.getState()==False:
                minTimes=2**32
                pm_i=0
                thisidea=None
                rm_i=0
                for j,pm in enumerate(PM):
                    if not pm.is_empty():
                        idea,ind=pm.nextIdea(coder.systemTime)

                        if not idea:
                            continue
                        if idea.needTimes<minTimes and idea.startTime<=coder.systemTime:
                            minTimes=idea.needTimes
                            pm_i=j
                            thisidea=idea
                            rm_i=ind
                if thisidea:
                    i+=1
                    idea=thisidea

                    PM[pm_i].popIdea(rm_i)
                    coder.setWorkState(True)
                    coder.TaskTimes=idea.needTimes
                    coder.startTime = coder.systemTime
                    IdeaStartTimes[idea.id]=coder.systemTime+coder.TaskTimes

            coder.systemTime+=1
            coder.updateState()
    return IdeaStartTimes

if __name__ == '__main__':
    N=2
    M=2
    P=[ [1, 1, 1, 2],
        [1, 2, 1, 1],
        [1, 3, 2, 2],
        [2, 1, 1, 2],
        [2, 3, 5, 5],]

    print(solver(N,M,P))




