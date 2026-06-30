class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        left = right = 0
        freq = dict()
        cnt = 0
        n = len(s)
        while right < n:
            char = s[right]
            freq[char] = freq.get(char,0) + 1
            while len(freq) == 3:
                cnt += n - right
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    freq.pop(s[left])
                left += 1
            right += 1
        return cnt
