class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows=len(matrix)
        cols=len(matrix[0])

        r=[False for i in range(rows)]
        c=[False for i in range(cols)]

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]==0:
                    r[i]=True
                    c[j]=True

        for i in range(len(r)):
            for j in range(len(c)):
                if r[i]==True or c[j]==True:
                    matrix[i][j]=0
        