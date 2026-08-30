class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        mini,maxi = nums.index(min(nums)),nums.index(max(nums))
        return min(max(mini,maxi) + 1,n-min(mini,maxi),(mini + 1) + (n-maxi),(maxi + 1)+(n - mini))
    

        