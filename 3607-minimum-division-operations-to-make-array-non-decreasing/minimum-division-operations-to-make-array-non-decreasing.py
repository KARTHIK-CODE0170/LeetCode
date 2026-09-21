import math
from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        # Traverse from right to left
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] > nums[i + 1]:
                min_divisor = self._get_min_divisor(nums[i])
                # If even the smallest divisor is still greater than the next element, it's impossible
                if min_divisor > nums[i + 1]:
                    return -1
                nums[i] = min_divisor
                ans += 1
        return ans

    def _get_min_divisor(self, num: int) -> int:
        # Find the smallest proper divisor (smallest prime factor)
        for divisor in range(2, math.isqrt(num) + 1):
            if num % divisor == 0:
                return divisor
        return num