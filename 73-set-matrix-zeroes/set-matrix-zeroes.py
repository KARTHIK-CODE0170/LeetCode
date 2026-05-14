class Solution:
    def rowsetter(self,matrix,m,n,rownumber)->None:
        for i in range(n):
            matrix[rownumber][i] = 0
    def colsetter(self,matrix,m,n,colnumber)->None:
            for i in range(m):
                matrix[i][colnumber] = 0
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix),len(matrix[0])
        colarr = [0] * n
        rowarr = [0] * m
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rowarr[i] , colarr[j] = 1, 1
        for i in range(m):
            if(rowarr[i] == 1):
                self.rowsetter(matrix,m,n,i)
        for i in range(n):
            if(colarr[i] == 1):
                self.colsetter(matrix,m,n,i)