class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        low, high = 1, n -2
        if nums[low] != nums[low-1]:
            return nums[low -1]
        if nums[high] != nums[high + 1]:
            return nums[high + 1]
        while low <= high:
            mid = (high - low) // 2 + low
            if nums[mid-1] != nums[mid] and nums[mid] != nums[mid + 1]:
                return nums[mid]
            elif (mid % 2 != 0 and nums[mid - 1] == nums[mid]) or (mid % 2 == 0  and nums[mid  + 1] == nums[mid]) :
                low = mid + 1
            else:
                high = mid - 1 
    