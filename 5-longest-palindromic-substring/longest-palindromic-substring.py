class Solution:
    def check(self,left,right,arr,s):
        maxi = 0
        while left > -1 and right < len(s):
            if s[left] != s[right]:
                break
            maxi =( right - left + 1)
            left -= 1
            right += 1
        arr[0],arr[1],arr[2] = left+1,right - 1,maxi
        
    def longestPalindrome(self, s: str) -> str:
        right = 0
        res = ""
        maxi = 0
        arr = [0] * 3
        while right < len(s):
            self.check(right,right,arr,s)
            if arr[2] > maxi:
                maxi = arr[2]
                res = s[arr[0]:(arr[0] + arr[2])]
            self.check(right,right + 1,arr,s)
            if arr[2] > maxi:
                maxi = arr[2]
                res = s[arr[0]:arr[0] + arr[2]]
            right += 1
        return res
            
            