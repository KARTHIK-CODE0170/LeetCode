class Solution:
    def check(self,arr:List[List[int]], i , j) -> bool:
        x = arr[i].count(1)
        if x != 1:
            return False
        # check the column
        cnt = 0
        for z in range(len(arr)):
            if arr[z][j] == 1:
                cnt += 1
        return cnt == 1
    def numSpecial(self, mat: List[List[int]]) -> int:
        cnt = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    if self.check(mat, i, j):
                        cnt += 1
        return cnt