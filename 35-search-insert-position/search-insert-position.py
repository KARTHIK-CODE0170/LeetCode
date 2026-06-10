class Solution:
    def fun(self,arr,low,high,k,ans):
        if low > high:
            return ans
        mid = (high - low) // 2 + low
        if arr[mid] == k:
            return mid
        elif arr[mid] < k:
            return self.fun(arr,mid + 1,high,k,mid + 1)
        else:   
            return self.fun(arr,low,mid - 1,k , mid)

    
    def searchInsert(self, nums: List[int], target: int) -> int:
        ans = 0
        ans = self.fun(nums,0,len(nums)-1,target,len(nums))
        return ans

        