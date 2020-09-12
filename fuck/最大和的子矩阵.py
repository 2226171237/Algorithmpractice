
# 在一个二维矩阵种扎到和最大的子矩阵。
def getMaxSubArray(nums):
    '''一维数组的连续最大和'''
    dp=nums[0]
    maxSum=0
    for i in range(1,len(nums)):
        if dp>0:
            dp=dp+nums[i]
        else:
            dp=nums[i]
        maxSum=max(maxSum,dp)
    return maxSum

# 求最大子矩阵
# 穷举行数为 1 行，2 行，3，。。。M行的子矩阵，得到最大和 ，n行相加得到一位数组，然后求最大连续子数组的和
def getMaxSubMatrixSum(matrix):
    temp_matrix=matrix.copy()
    maxSum=0
    for i in range(len(matrix)-1,-1,-1):  # O(M)
        maxSum = max(maxSum, getMaxSubArray(temp_matrix[i]))
        row=i-1
        while row>=0:  # O(log(M))
            for j in range(len(temp_matrix[0])): # O(N)
                temp_matrix[i][j]+=temp_matrix[row][j]
            maxSum = max(maxSum, getMaxSubArray(temp_matrix[i])) # O(N)
            row-=1
    return maxSum         # O(Mlog(M)N)


matrix=[[0,-2,-7,0],
        [9,2,-6,2],
        [-4,1,-4,1],
        [-1,8,0,-2]]

print(getMaxSubMatrixSum(matrix))


