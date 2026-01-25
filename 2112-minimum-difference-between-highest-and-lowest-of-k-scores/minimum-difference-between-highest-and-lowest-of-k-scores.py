class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        right = n - 1
        cnt = float('inf')
        if(n <= 1):
            return 0
        for i in range(n-k+1):
            cnt = min(cnt,nums[i + k -1 ]-nums[i])
            # right -= 1
        return cnt if(cnt != float('inf')) else 0
