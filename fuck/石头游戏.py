
'''
你和你的朋友面前有一排石头堆，用一个数组 piles 表示，piles[i] 表示第 i 堆石子有多少个。
你们轮流拿石头，一次拿一堆，但是只能拿走最左边或者最右边的石头堆。
所有石头被拿完后，谁拥有的石头多，谁获胜。
'''
def playStoneGame(piles):
    N=len(piles)
    first=[[0 for _ in range(N)] for _ in range(N)]  # 先手，dp[i][j]  pile_i... pile_j 堆先手可以获得的最大收益
    second=[[0 for _ in range(N)] for _ in range(N)] # 后收，dp[i][j]  pile_i... pile_j 堆后手可以获得的最大收益

    # 只有一堆的情况
    for i in range(N):
        first[i][i]=piles[i]

    for jj in range(1,N):
        for i in range(0,N-jj):
            j=i+jj
            left=piles[i]+second[i+1][j]
            right=piles[j]+second[i][j-1]
            if left>right:
                first[i][j]=left
                second[i][j]=first[i+1][j]
            else:
                first[i][j]=right
                second[i][j]=first[i][j-1]
    return first[0][-1],second[0][-1]

print(playStoneGame([3,9,1,2]))