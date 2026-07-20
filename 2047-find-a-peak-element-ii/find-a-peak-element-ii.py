class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        i = j = 0
        m,n = len(mat), len(mat[0])
        while i < m and j < n:
            curr = mat[i][j]
            maxi = curr
            ni,nj = i ,j 
            #right
            if j + 1 < n:
                if maxi < mat[i][j + 1]:
                    nj = j + 1
                    maxi = mat[i][j+1]
            #left
            if j - 1 >= 0:
                if maxi < mat[i][j - 1]:
                    nj = j - 1
                    maxi = mat[i][nj]
            #top
            if i - 1 >= 0:
                if maxi < mat[i - 1][j]:
                    ni = i - 1
                    maxi = curr = mat[ni][j]
            #bottom
            if i + 1 < m:
                if maxi < mat[i + 1][j]:
                    ni = i + 1
                    maxi = mat[ni][j]
            if ni == i and nj == j:
                return [i,j]

            i, j = ni , nj

