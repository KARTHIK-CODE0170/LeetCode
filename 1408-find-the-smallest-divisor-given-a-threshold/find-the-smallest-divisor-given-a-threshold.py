import math
class Solution:
    def fun(self,arr,div,k):
        cnt = 0
        for i in arr:
           cnt += math.ceil(i/div) 
        if cnt <= k:
            return True
        return False

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low = 1
        high = max(nums)
        ans = float("inf")
        while low <= high:
            mid = (high - low) //2 + low
            if self.fun(nums,mid,threshold):
                ans = min(ans,mid)
                high = mid - 1
            else:
                low = mid + 1
        return ans