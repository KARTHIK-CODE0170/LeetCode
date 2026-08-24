class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        def isPrime(x):
            if x < 2:
                return False
            if x == 2 or x == 3 :
                return True
            if x % 2 == 0 or x % 3 == 0:
                return False
            for i in range(5,int(sqrt(x))  +1,6):
                if x % i == 0 or (x % (i + 2) == 0) :
                    return False
            return True
        left,right = 0,0
        for i in range(len(nums)):
            if isPrime(nums[i]):
                left = i
                break
        for i in range(len(nums)-1,-1,-1):
            if isPrime(nums[i]):
                right = i
                break
        return right - left