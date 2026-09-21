class Solution:
    def primePalindrome(self, n: int) -> int:
        def is_prime(x: int) -> bool:
            if x < 2:
                return False
            if x % 2 == 0:
                return x == 2
            i = 3
            while i * i <= x:
                if x % i == 0:
                    return False
                i += 2
            return True

        # Handle edge cases for small numbers
        if 8 <= n <= 11:
            return 11

        # Generate palindromes by length. 
        # Note: All even-length palindromes greater than 11 are multiples of 11, so we can skip them.
        for length in range(1, 10):
            if length % 2 == 0 and length > 2:
                continue
            
            half = 10 ** ((length - 1) // 2)
            for root in range(half, half * 10):
                s = str(root)
                if length == 1:
                    candidate = int(s)
                else:
                    candidate = int(s + s[-2::-1])
                
                if candidate >= n and is_prime(candidate):
                    return candidate