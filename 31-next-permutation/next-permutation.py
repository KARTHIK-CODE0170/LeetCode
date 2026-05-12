class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        cnt = 0
        if len(nums) == 1:
            return 
        #find the decrease in from the right side
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i] and j >= 0:
                j -= 1
            nums[i],nums[j] = nums[j],nums[i]
        nums[i + 1:] = reversed(nums[i+ 1:])
        return nums
        

        


