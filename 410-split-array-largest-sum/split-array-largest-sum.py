class Solution:
    def fun(self,arr,mid,k):
        ecnt = esum = r = 0
        while r < len(arr):
            if arr[r] > mid:
                return False
            if esum + arr[r] > mid:
                ecnt += 1
                esum = arr[r]
            else:
                esum += arr[r]
            r += 1
        ecnt += 1
        return ecnt <= k
    def splitArray(self, nums: List[int], k: int) -> int:
        low, high = 0, sum(nums)
        while low <= high:
            mid = (high - low)//2 + low
            if self.fun(nums,mid,k):
                high = mid - 1
            else:
                low = mid + 1
        return low
        