class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        con = set(nums)
        cnt = 0
        maxi = 0
        if len(nums) == 0:
            return 0
        for num in con:
            x = num
            if x - 1 not in con:
                while x + 1 in con:
                    cnt += 1
                    x = x + 1
            maxi = max(maxi,cnt)
            cnt = 0
        return maxi + 1
