class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        right = 0
        maxSum = float('-inf')
        currSum = 0
        for i in nums:
            currSum += i
            maxSum = max(maxSum,currSum)
            if currSum < 0:
                currSum = 0
        return maxSum
