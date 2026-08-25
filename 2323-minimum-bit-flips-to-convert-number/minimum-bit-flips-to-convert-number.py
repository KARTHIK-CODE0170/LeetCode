class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        cnt = 0
        while start != 0 or goal !=0 :
            if start & 1 != goal & 1:
                cnt += 1
            start >>=1
            goal >>= 1
        return cnt
        