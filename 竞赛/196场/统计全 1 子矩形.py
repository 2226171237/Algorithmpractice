'''

'''

def find(P,j):
    cnt=0
    for k in range(j,-1,-1):
        if P[k]==0:
            return cnt
        else:
            h=min(P[k:j+1])
            cnt+=h
    return cnt

class Solution(object):
    def numSubmat(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        rows,cols=len(mat),len(mat[0])
        P=[[0 for _ in range(cols)] for _ in range(rows)]

        for j in range(cols):
            P[0][j]=mat[0][j]

        for i in range(1,rows):
            for j in range(cols):
                if mat[i][j]:
                    P[i][j]=P[i-1][j]+1

        cnt=0
        for i in range(rows):
            for j in range(cols):
                if P[i][j]:
                    cnt+=find(P[i],j)

        return cnt

if __name__ == '__main__':
    s=Solution()
    print(s.numSubmat([[1,1,1,1,1,1]]))
