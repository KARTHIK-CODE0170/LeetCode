class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        arr = [0] * 26
        for i in s:
            arr[ord(i) % 97] += 1
        for i in t:
            arr[ord(i) % 97] -= 1
        
        return False if any(arr) else True


        