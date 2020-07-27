

def getLongestInceaseSubSequence(arr):
    '''
    获得连续最长上升子序
    动态规划，P(i) 表示arr[:i+1] 以arr[i]为结尾的最长上升子序
    :param arr:
    :return:
    '''
    N=len(arr)
    if N==0:
        return 0
    maxLen=1
    P=[1 for _ in range(N)]
    i=1
    while i<N:
        if arr[i]>arr[i-1]:
            P[i]=P[i-1]+1
        maxLen=max(maxLen,P[i])
        i+=1
    return maxLen



def getLongestInceaseSubSequence2(arr):
    '''
    获得非连续最长上升子序
    动态规划，P(i) 表示arr[:i+1] 以arr[i]为结尾的最长上升子序
    :param arr:
    :return:
    '''
    N = len(arr)
    if N == 0:
        return 0
    maxLen = 1
    P = [1 for _ in range(N)]
    i = 1
    while i < N:
        maxT=0
        for j in range(i):
            if arr[j]<arr[i]:
                maxT=max(maxT,P[j])
        P[i]=maxT+1
        maxLen = max(maxLen, P[i])
        i += 1
    return maxLen

print(getLongestInceaseSubSequence2([9,2,5,3,6,7]))