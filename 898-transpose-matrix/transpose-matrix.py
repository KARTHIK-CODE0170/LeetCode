class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row , col = len(matrix),len(matrix[0])
        res = []
        for i in range(col):
            new_arr = []
            for j in range(row):
                new_arr.append(matrix[j][i])
            res.append(new_arr)
        return res