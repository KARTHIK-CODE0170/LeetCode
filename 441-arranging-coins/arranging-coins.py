class Solution:
    def tell(self,n):
        return (n*(n+1))//2
    def fun(self,low,high,n):
        while (low <= high):
            mid = (high - low)//2 + low
            x = self.tell(mid)
            if x == n:
                return mid
            elif x < n:
                low = mid + 1
            else:
                high = mid - 1
        return low -1


    def arrangeCoins(self, n: int) -> int:
        low,high = 1,n//2 + 1
        return self.fun(low,high,n)
        