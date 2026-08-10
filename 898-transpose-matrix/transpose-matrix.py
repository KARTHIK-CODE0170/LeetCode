class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ans = []
        for i in zip(*matrix):
            ans.append(i)
        return ans