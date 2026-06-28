class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0,0
        freq = dict()
        maxi = 0
        while r < len(s):
            char = s[r]
            freq[s[r]] = freq.get(s[r],0) + 1
            while len(freq) < (r - l + 1):
                freq[s[l]] -= 1
                if freq[s[l]] == 0:
                    freq.pop(s[l])
                l += 1
            maxi = max(maxi,r - l + 1)
            r += 1
        return maxi 

            
