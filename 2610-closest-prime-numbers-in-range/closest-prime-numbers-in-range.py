class Solution:
    def god(self,right):
        # right += 1
        arr = [True] * (right + 1)
        arr[0] = arr[1] = False
        i = 2
        while i * i <= right:
            for j in range(i * i,right+1,i):
                arr[j] = False
            i += 1
        return arr


    def closestPrimes(self, left: int, right: int) -> List[int]:
        res = []
        arr = self.god(right)
        for i in range(left,right + 1):
            if arr[i]:
                res.append(i)
        i = 1
        min_diff = 10**5
        ans = [-1,-1]
        while i < len(res):
            min_val = res[i] - res[i - 1]
            if (min_val) == min_diff:
                i += 1
                continue
            if (min_val) < min_diff:
                ans[0],ans[1]  = res[i-1],res[i]
                min_diff = min_val
            i += 1
        return ans
