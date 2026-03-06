class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        left = right = 0
        if(s.count('1') == 1):
            return True
        else:
            i = s.find('1')
            while(i < len(s) and s[i] == '1'):
                i+= 1
            if(s[i:].find('1') != -1):
                return False
                
        return True

        #Most optimal one
# class Solution:
#     def checkOnesSegment(self, s: str) -> bool:
#         return "01" not in s
            