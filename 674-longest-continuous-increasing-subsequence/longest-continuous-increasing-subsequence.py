class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        l, r = 0 ,1
        ans = 0
        while r < n:
            if nums[r] <= nums[r - 1]:
                ans = max(ans,r - l)
                l = r
            r += 1
        ans =max(ans,r - l)
        return 0 if ans == 0 else ans
