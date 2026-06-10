class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        pre = 1
        suff = 1
        ans = float('-inf')
        for i in range (n):
            pre *= nums[i]
            suff *= nums[n - i - 1]
            ans = max(ans,pre,suff)
            if pre == 0:
                pre = 1
            if suff == 0:
                suff = 1
        return ans