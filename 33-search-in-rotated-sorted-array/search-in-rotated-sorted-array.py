class Solution:
    def fun(self,arr,low,high,k):
        if low <= high:
            mid = (high - low) //2 + low
            if arr[mid] == k:
                return mid
            elif arr[mid] > k:
                return self.fun(arr,low,mid - 1,k)
            else:
                return self.fun(arr,mid + 1,high,k)
        else:
            return -1


    def search(self, nums: List[int], target: int) -> int:
        
        #find the rotated index
        idx = len(nums) -1
        

        for i in range(1,len(nums)):
            if nums[i] < nums[i - 1]:
                idx = i
                break

        if target <= nums[-1] and target >= nums[idx]:
            return  self.fun(nums,idx,len(nums)-1,target)
        elif target >= nums[0] and target <= nums[idx - 1]:
            return self.fun(nums,0,idx -1,target)
        else:
            return -1 
        