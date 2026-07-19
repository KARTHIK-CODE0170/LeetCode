class Solution:
    def fun(self,arr,low,high,tar):
        while low <= high:
            mid = (high + low) //2
            if arr[mid] == tar:
                return True
            elif arr[mid] < tar:
                low = mid + 1
            else:
                high = mid - 1
        return False
    def searchMatrix(self, mat: List[List[int]], target: int) -> bool:
        up, down = 0 , len(mat) - 1
        n = len(mat[0])
        while up <= down:
            mid = (up + down) // 2
            if mat[mid][0] <= target <= mat[mid][n - 1]:
                if self.fun(mat[mid],0,n-1,target):
                    return True
                else:
                    return False
            elif target < mat[mid][0]:
                down = mid - 1
            else:
                up = mid + 1
            
        return False
