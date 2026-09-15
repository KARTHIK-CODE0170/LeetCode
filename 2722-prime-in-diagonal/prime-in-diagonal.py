class Solution:
    def isPrime(self,x):
        if x < 2:
            return False
        if x == 2 or x == 3:
            return True
        if x % 2 == 0 or x % 3 == 0:
            return False
        i = 5
        while i * i <= x:
            if x % i == 0 or x %(i + 2) == 0:
                return False
            i += 6
        return True
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        maxi = 0
        n = len(nums)
        for i in range(n):
            if self.isPrime(nums[i][i]):
                maxi = max(maxi,nums[i][i])
            if self.isPrime(nums[i][n-i-1]):
                maxi = max(maxi,nums[i][n-i-1])
        return maxi