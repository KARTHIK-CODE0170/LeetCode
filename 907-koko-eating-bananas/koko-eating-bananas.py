import math
class Solution:
    def fun(self,arr,ele):
        ans = 0
        for i in arr:
            ans += math.ceil(i/ele)
        return ans
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        while low <= high:
            mid = (high + low) //2
            if self.fun(piles,mid) <= h:
                high = mid - 1
            else:
                low = mid + 1
        return low