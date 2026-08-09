class Solution:
    def largestOddNumber(self, num: str) -> str:
        odd_number = {
            '1' : True,
            '3' : True,
            '5' : True,
            '7' : True,
            '9' : True
        }
        
        for j in range(len(num) - 1,-1,-1):
            if odd_number.get(num[j],False):
                return num[:j+1]
        return ""