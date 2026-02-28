class Solution:
    def concatenatedBinary(self, n: int) -> int:
        st = ""
        mod = 10**9 + 7
        for i in range(1,n + 1):
            x = bin(i)
            st += x[2:]
        ans = int(st,2) % mod
        return ans

