class Solution:
    def fun(self,n):
        arr = [True] * (n )
        # res = []
        i = 2
        while i * i <= n:
            if arr[i]:
                for j in range(i * i,n,i):
                    arr[j] = False
            i += 1
        return arr
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        cnt = 0
        res = self.fun(n)
        res[0] = res[1] = False
        return sum(res)