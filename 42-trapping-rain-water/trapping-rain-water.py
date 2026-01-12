class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0,len(height) - 1
        res = 0
        maxL, maxR = height[l], height[r]
        while l < r:
            if maxL <= maxR:
                res += max(0,min(maxL,maxR) - height[l])
                l += 1
                maxL = max(maxL,height[l])
            else:
                res += max(0,min(maxL,maxR) - height[r])
                r -= 1
                maxR = max(maxR,height[r])
        
        return res
            