class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        x = 1
        i = 0
        while True:
            if x == n:
                return True
            elif x > n:  
                return False
            else:
                x = x << 1