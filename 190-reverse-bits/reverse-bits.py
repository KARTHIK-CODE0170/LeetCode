class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for _ in range(32):
            bit = ans << 1
            ans = (n & 1) | bit
            # ans = 
            n = n >> 1
        return ans