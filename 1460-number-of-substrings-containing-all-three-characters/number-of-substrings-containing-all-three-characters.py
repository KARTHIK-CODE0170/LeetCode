class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        freq = dict()
        left,right = 0,0
        n = len(s)
        cnt = 0
        while right < len(s):
            freq[s[right]] = freq.get(s[right],0) + 1

            while len(freq) == 3:
                cnt += n - (right - left + 1) + 1
                n-=1
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    freq.pop(s[left])
                left += 1
            right += 1
        return cnt


