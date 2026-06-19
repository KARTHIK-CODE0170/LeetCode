class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = float("-inf")
        low = 0
        high = len(height) -1
        while(low < high):
            res = max(res,min(height[low],height[high]) * (high - low))
            if height[low] <= height[high]:
                low += 1
            else:
                high -= 1
        return res
        