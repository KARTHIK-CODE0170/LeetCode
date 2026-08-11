class Solution:
    def prime(self,n):
        arr = []
        for i in range(n + 1):
            arr.append(i)
        i = 2
        while i * i <= (n + 1):
            if i == arr[i]:
                j = i * i
                while j <= n:
                    arr[j] = i
                    j += i
            i += 1
        return arr

    def distinctPrimeFactors(self, nums: List[int]) -> int:
        prime_number = self.prime(max(nums))

        p = dict()
        for i in nums:
            while i > 1:
                p[prime_number[i]]  = p.get(prime_number[i],0) + 1
                i //= prime_number[i]
        return len(p)