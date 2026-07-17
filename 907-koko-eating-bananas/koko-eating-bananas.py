import math as m
class Solution:
    def fun(self,arr,mid,hr):
        cnt = 0
        for i in arr:
            cnt += m.ceil(i/mid)
        return cnt <= hr 

    def minEatingSpeed(self, arr: List[int], h: int) -> int:
        l, hi = 1 ,max(arr)
        while l <= hi:
            mid = (hi - l) // 2 + l
            if self.fun(arr,mid,h):
                hi = mid - 1
            else:
                l = mid + 1
        return l