class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        rows=len(matrix)
        cols=len(matrix[0])

        # #Space=O(m + n) space Time=O(n*m)
        # r=[False for i in range(rows)]
        # c=[False for i in range(cols)]

        # for i in range(rows):
        #     for j in range(cols):
        #         if matrix[i][j]==0:
        #             r[i]=True
        #             c[j]=True

        # for i in range(len(r)):
        #     for j in range(len(c)):
        #         if r[i]==True or c[j]==True:
        #             matrix[i][j]=0


        rowZero=False

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c]==0:
                    matrix[0][c]=0
                    if r>0:
                        matrix[r][0]=0
                    else:
                        rowZero=True

        for r in range(1,rows):
            for c in range(1,cols):
                if matrix[0][c]==0 or matrix[r][0]==0:
                    matrix[r][c]=0
        
        if matrix[0][0]==0:
            for r in range(rows):
                matrix[r][0]=0
        
        if rowZero:
            for c in range(cols):
                matrix[0][c]=0

        