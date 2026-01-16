class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        right = 0
        sum1 = 0
        best = float('-inf')
        while right < len(nums):
            sum1 += nums[right]
            best = max(sum1,best)
            if(sum1 < 0):
                sum1 = 0
            right += 1
        return best