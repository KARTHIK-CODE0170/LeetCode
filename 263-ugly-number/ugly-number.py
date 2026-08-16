class Solution:
    def isUgly(self, n: int) -> bool:
        prime = (2,3,5)
        for i in prime:
            while n >= 1:
                if n % i == 0:
                    n = n // i
                else:
                    break
        return True if n == 1 else False 
        