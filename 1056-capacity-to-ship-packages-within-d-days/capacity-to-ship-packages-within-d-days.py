class Solution:
    def fun(self,arr,days,mid):
        day = 0
        i = 0
        cap = 0
        while i < len(arr):
            cap += arr[i]
            if cap > mid:
                day += 1
                cap = 0
                continue
            i += 1
        if cap > 0:
            day += 1
        return day <= days
        
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        ans = 0
        while low <= high:
            mid = (high - low)//2 + low
            if self.fun(weights,days,mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans