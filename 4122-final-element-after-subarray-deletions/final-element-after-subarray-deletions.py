class Solution:
    def finalElement(self, nums: List[int]) -> int:
        arr = nums
        
        if len(arr) == 1:
            return arr[0]
        
        return max(arr[0], arr[-1])