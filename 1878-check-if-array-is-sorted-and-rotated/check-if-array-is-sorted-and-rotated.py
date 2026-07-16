class Solution:
    def check(self, nums: List[int]) -> bool:
        cnt = 0
        if len(nums) == 1:
            return True
        for i in range(len(nums)):
            if nums[i] > nums[(i + 1)% len(nums) ] :
                cnt += 1
        return cnt<= 1
            
        