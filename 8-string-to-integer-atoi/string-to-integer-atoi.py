class Solution:
    def myAtoi(self, s: str) -> int:
        def check_empty(x):
            if len(x) == 0:
                return 1
            else:
                return 0
        # def x(ans,sign):
        #     if sign == - 1:
        #         return 
        ans = 0
        if check_empty(s):
            return 0

        MIN = -2**31
        MAX = (2** 31) - 1
        i = 0
        while i < len(s) and (s[i] == ' '):
            i += 1

        s = s[i:]
        i = 0
        if check_empty(s):
            return 0
        # ---------------------------------
        sign = int()
        if s[0] == '-':
            sign = -1
            i += 1
        elif s[0] == '+':
            sign = 1
            i += 1
        elif not s[0].isdigit():
            return 0
        #-------------------------------------
        while i < len(s):
            if s[i] == '0':
                i += 1
            break

        while i < len(s):
            if s[i].isdigit():
                ans = ans * 10 + int(s[i])
            else:
                break
            i += 1
        if sign == -1:
            ans *= -1
        if ans > MAX:
            ans = MAX
        elif ans < MIN:
            ans = MIN
        
            # return -ans
        return ans
                
            
            
        
