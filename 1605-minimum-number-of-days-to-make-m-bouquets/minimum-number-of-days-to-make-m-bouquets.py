class Solution:
    def possible(self,arr,k,flow):
        #k ->adjacent flowers
        #flow = mid for mthe main function
        cnt = 0
        res = 0
        for i in arr:
            if i <= flow:
                cnt += 1
            else:
               res += cnt // k
               cnt = 0 
        res =  res + (cnt // k)
        return res
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        low = min(bloomDay)
        high = max(bloomDay)
        res = float("inf")
        while low <= high:
            mid = (high - low)//2  + low
            res = self.possible(bloomDay,k,mid)
            if res >= m:
                high = mid - 1
            else:
                low = mid + 1
        return low

        
        