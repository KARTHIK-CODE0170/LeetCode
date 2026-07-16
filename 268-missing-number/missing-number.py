class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        a = 1
        b = 1
        for i in range(len(nums)):
            a ^= nums[i]
            b ^= i
        b ^= len(nums)
        return a ^ b