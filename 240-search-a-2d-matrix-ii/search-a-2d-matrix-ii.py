class Solution:
    def searchMatrix(self, mat: List[List[int]], target: int) -> bool:
        m = len(mat)
        n = len(mat[0])
        row, col = m - 1, 0
        while row > -1 and col < n :
            
            if  mat[row][col] == target:
                return True
            elif target <  mat[row][col]:
                row = row - 1
                # curr = mat[row][col]
            else:
                col = col + 1
                
        return False


