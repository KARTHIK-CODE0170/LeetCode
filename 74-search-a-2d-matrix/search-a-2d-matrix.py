class Solution:
    def searchMatrix(self, mat: List[List[int]], target: int) -> bool:
        up, down = 0 , len(mat) - 1
        n = len(mat[0]) -1
        while up <= down:
            mid = (up + down) // 2
            if target in mat[mid]:
                return True
            elif target < mat[mid][0]:
                down = mid - 1
            else:
                up = mid + 1
            
        return False
