class Solution:
    def trailingZeroes(self, n: int) -> int:
        i = 1
        cnt = 0
        while True:
            x = n//(5 ** i) 
            if x == 0:
                return cnt
            cnt += x
            i += 1
        return cnt
            
        