class Solution:
    def check(slef,s,left,right,arr):
        maxi = 1
        while left >= 0 and right < len(s):
            if s[left] != s[right]:
                break
            maxi = max(right - left + 1,maxi)
            left -= 1
            right += 1
            
        arr[0],arr[1],arr[2] = left+1,right-1,maxi
        return None
    def longestPalindrome(self, s: str) -> str:
        left = right = 0
        res = ""
        arr = [0] * 3
        maxi = 0
        for i in range(len(s)):
            self.check(s,i,i,arr)
            if arr[2] > maxi:
                maxi = arr[2]
                res = s[arr[0]:arr[0] + arr[2]]
            self.check(s,i,i + 1,arr)
            if arr[2] > maxi:
                maxi = arr[2]
                res = s[arr[0]:arr[0] + arr[2]]
        return res