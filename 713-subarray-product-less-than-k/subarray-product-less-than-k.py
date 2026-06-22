class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0    
        ans = 1
        cnt = 0
        left,right = 0,0
        n = len(nums)
        while right < len(nums):
            ans *= nums[right]
            while ans >= k:
                ans = ans // nums[left]
                left += 1
            cnt += (right - left + 1)
            right += 1
        return cnt
