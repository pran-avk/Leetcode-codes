class Solution(object):
    def setZeroes(self, matrix):
        a=[1]*len(matrix)
        b=[1]*len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    a[i]=0
                    b[j]=0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if a[i]==0 or b[j]==0:
                    matrix[i][j]=0
        return matrix
        