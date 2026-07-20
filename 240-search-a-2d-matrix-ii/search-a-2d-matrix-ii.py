class Solution:
    def searchMatrix(self, mat: List[List[int]], target: int) -> bool:
        m = len(mat)
        n = len(mat[0])
        row, col = m - 1, 0
        curr = mat[row][col]
        while row > -1 and col < n :
            curr = mat[row][col]
            if curr == target:
                return True
            elif target < curr:
                row = row - 1
                # curr = mat[row][col]
            elif target > curr:
                col = col + 1
                
        return False


