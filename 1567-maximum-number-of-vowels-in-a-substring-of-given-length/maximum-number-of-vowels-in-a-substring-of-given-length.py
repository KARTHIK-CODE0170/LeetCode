class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = {'a','e','i','o','u'}
        left = 0
        right = 0
        cnt = 0
        maxi = 0
        while right < len(s):
            if s[right] in vowel:
                cnt += 1

            if (right - left + 1) == k:
                maxi = max(maxi,cnt)
                if s[left] in vowel:
                    cnt -= 1
                left +=1
            right += 1
        return maxi