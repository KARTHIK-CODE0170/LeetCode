import math as mp
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        return mp.gcd((n*(n + 1)),n * n)
