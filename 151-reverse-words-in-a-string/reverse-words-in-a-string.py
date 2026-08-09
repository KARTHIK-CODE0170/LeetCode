class Solution:
    def reverseWords(self, s: str) -> str:
        # s = "  hello world  "
        res = []
        j = len(s) - 1
        while s[j] == " ":
            j-= 1
        i = j
        while i > -1:
            while s[i] != " " and i > -1:
                i -= 1
            res.append(s[i + 1:j + 1])
            while s[i] == " ":
                i -= 1
            j = i 
        # if i == -1:
        #     res.append(s[i + 1,j + 1])
        return ' '.join(res)


        #or
        '''
        arr = s.split()
        arr.reverse()
        return ' '.join(arr)
        '''
            



            