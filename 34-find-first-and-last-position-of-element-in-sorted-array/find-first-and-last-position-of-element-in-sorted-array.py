class Solution:
    def left(self,arr,low,high,lans,k):
        if low > high:
            return lans
        mid = (high - low) //2 + low
        if arr[mid] >= k:
            if(arr[mid] == k):
                lans = mid
            return self.left(arr,low,mid - 1,lans,k)
        else:
            return self.left(arr,mid + 1,high,lans,k)
    def right(self,arr,low,high,rans,k):
        if low > high:
            return rans
        mid = (high - low) //2 + low
        if arr[mid] <= k:
            if(arr[mid] == k):
                rans = mid
            return self.right(arr,mid + 1,high,rans,k)
        else:
            return self.right(arr,low,mid -1,rans,k)
    def searchRange(self, nums: List[int], target: int) -> List[int]:
         lans, rans = -1, -1
         return [self.left(nums,0,len(nums) -1,lans,target),self.right(nums,0,len(nums) -1,rans,target)]