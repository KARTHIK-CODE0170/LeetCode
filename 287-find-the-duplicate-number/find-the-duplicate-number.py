class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        visited = [False] * (len(nums) + 1)
        for i in nums:
            if visited[i]:
                return i
            visited[i] = True
        return 0
        