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

        p = set()
        for i in nums:
            while i > 1:
                p.add(prime_number[i])
                i //= prime_number[i]
        return len(p)



