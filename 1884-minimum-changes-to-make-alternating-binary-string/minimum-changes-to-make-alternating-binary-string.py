class Solution:
    def minOperations(self, s: str) -> int:
        One = 0
        x = len(s)
        for i in range(x):
            if((i % 2 == 0 and s[i] == '1') or (i % 2 != 0 and s[i] == '0')):
               One += 1
        return min(One,x - One)