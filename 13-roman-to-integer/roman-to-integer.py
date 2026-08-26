class Solution:
    def romanToInt(self, s: str) -> int:
        rtonum = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        i = 0
        res = 0
        while i < len(s) - 1:
            if rtonum[s[i]] < rtonum[s[i+1]]:
                res += (rtonum[s[i + 1]] - rtonum[s[i]])
                i = i + 2
            else:
                res += rtonum[s[i]]
                i = i + 1
        if i < len(s):
            res += rtonum[s[i]]
        return res
