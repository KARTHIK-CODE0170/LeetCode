class Solution:
    def check(slef,n):
        cnt = 0
        i = 1
        while i <(n + 1):
            if (n & i):
                cnt += 1
            i = i << 1
        return cnt
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n + 1):
            ans.append(self.check(i))
        return ans