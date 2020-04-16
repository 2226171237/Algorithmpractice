# -*-coding=utf-8 -*-
'''
如何对任务进行调度？
假设有一个中央调度机，有n个相同的任务需要调度到m台服务器上去执行，由于每台服务器的配置不一样，因此，服务器执行
一个任务所花费的时间也不同。现在假设第i个服务器执行一个任务所花费的时间为t[i]，例如有俩个执行机a与b,执行一个任
务分别需要7min，10min，有6个任务待调度。如果平分这六个任务，即a与b个执行三个，则最短需要30min完成所有。如何a分
4个，b分2个则最短28min完成。请设计调度算法，使得所有任务完成所需的时间最短。输入m台服务器，每台机器处理一个任务
的时间为t[i],完成n个任务，输出n个任务在m台服务器的分布：estimate_process_time(t,m,n)
'''
# 贪心算法来解决
# 对每台机器，计算机器已经分配任务的执行时间+这个任务需要的时间，选用最短时间的机器来进行处理。
def estimate_process_time(t,m,n):
    used=[0 for _ in range(m)]
    for _ in range(n):
        time=used[0]+t[0]
        sel_ind=0
        for i in range(m):
            if used[i]+t[i]<time:
                time=used[i]+t[i]
                sel_ind=i
        used[sel_ind]+=t[sel_ind]
    times=max(used)
    for i in range(m):
        used[i]/=t[i]
    return used,times


if __name__ == '__main__':
    t=[7,10]
    m=2
    n=6
    print(estimate_process_time(t,m,n))



